# -*- coding: utf-8 -*-
"""Exanima Turkce yama - surumden bagimsiz uygulayici.

NEDEN BAGLAM CAPASI:
  Onceki surum (tr_patch.py) metinleri exe icindeki OFFSET ile buluyordu. Oyun her
  guncellendiginde exe yeniden derlenir ve tum adresler kayar -> yama coker.
  Bu surum her metni adresle degil, KOMSULUKLA tanir: (kendi Ingilizce metni,
  bir onceki string sabiti, bir sonraki string sabiti). Bu ucluu yeniden derlemede
  degismez, cunku derleyici string sabitlerini ayni sirada yerlestirir.

ESLESME STRATEJISI (siki -> gevsek, ilk tutan kazanir):
  1. (en, prev, next) tam ucluu
  2. (en, prev)
  3. (en, next)
  4. sadece en  -- yalnizca exe'de tek bir kez geciyorsa (belirsizlik yoksa)

GUNCELLEME AKISI:
  Oyun guncellendiginde:
    python tr_patch2.py --rapor    -> eslesmeyenleri ve YENI cikan Ingilizce metinleri listeler
  Sonra tr_anchors.json elle guncellenir, tekrar calistirilir.

Delphi string sabiti bellek yapisi (dogrulanmis):
  [-16] refcount = FF*8 | [-8] uzunluk uint64 | [0] ASCII veri + null + 8'e hizalama dolgusu
  Tampon = align8(uzunluk+1). Yeni metin bu tampona sigmak zorunda.

Oyun fontunda Turkce glif yoksa metinler otomatik ASCII'ye cevrilir (--ascii, varsayilan acik).
Font duzeltilirse --turkce ile tam aksanli yazilir.
"""
import io
import json
import os
import re
import struct
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def kaynak_kok():
    """Veri dosyalarinin kok dizini.

    PyInstaller ile tek dosyaya paketlendiginde veri gecici bir dizine acilir
    ve yolu sys._MEIPASS'te durur; kaynaktan calisirken betigin yani basidir.
    """
    return getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


HERE = kaynak_kok()
ANCHORS = os.path.join(HERE, 'tr_anchors.json')

GAME = EXE = ORIG = None


def yolu_ayarla(oyun):
    """Oyun klasorunu belirler. Yukleyici acilista bir kez cagirir."""
    global GAME, EXE, ORIG
    GAME = oyun
    EXE = os.path.join(GAME, 'Exanima.exe')
    ORIG = EXE + '.orijinal'


yolu_ayarla(r'E:\Steam\steamapps\common\Exanima')

# Metin sabitleri yalnizca ASCII degil: CP1252 '…' (0x85), paragraf ayraci olarak
# yalin CR ve 200 bayttan uzun ogretici metinler de var. Ilk surumun dar deseni
# bunlari hic gormedigi icin karakter secim aciklamalari cevrilmemisti.
PAT = re.compile(rb'\xff{8}(.{8})([\x20-\x7e\x80-\xff\r\n\t]{1,3000})\x00', re.S)

# Cevrilmemesi gereken teknik metinler (gomulu GLSL golgelendiricileri)
GLSL = re.compile(r'void main\(\)|uniform |gl_Position|FragColor|sampler2D|#version')

# Ana menu ve karakter unvanlari "gravur" stiliyle ciziliyor: bu ekranlar HARF
# DISINDA hicbir sey gostermiyor (noktalama ve aksanli harfler dahil, ampirik
# olarak dogrulandi). Bu metinler ASCII Turkce kalir; oyunun geri kalani tam
# Turkce (CP1254) yazilir.
STYLIZED = {
    'BEGIN', 'CONTINUE', 'ARENA', 'MANUAL', 'SETTINGS', 'EXIT', 'EXIT;',
    'NEW CAREER', 'PRACTICE', 'BACK', 'NEW GAME', 'FORFEIT', 'NOVICE',
    'EXPERT', 'RESTART', 'NEXT FIGHT',
    'UNKNOWN', 'KNIGHT', 'PROCTOR', 'VILLAGER',
}

TRMAP = str.maketrans({
    'ç': 'c', 'Ç': 'C', 'ğ': 'g', 'Ğ': 'G', 'ı': 'i', 'İ': 'I',
    'ö': 'o', 'Ö': 'O', 'ş': 's', 'Ş': 'S', 'ü': 'u', 'Ü': 'U',
    'â': 'a', 'Â': 'A', 'î': 'i', 'Î': 'I', 'û': 'u', 'Û': 'U',
})


def align8(n):
    return ((n + 7) // 8) * 8


def scan(data):
    """[(veri_offset, metin, tampon_boyutu)] - adres sirali."""
    out = []
    for m in PAT.finditer(data):
        declared = struct.unpack('<Q', m.group(1))[0]
        raw = m.group(2)
        if declared == len(raw):
            out.append((m.start() + 16, raw.decode('latin-1'), align8(declared + 1) - 1))
    out.sort()
    return out


def build_index(items):
    by3, by_prev, by_next, by_en = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
    for i, (off, txt, cap) in enumerate(items):
        prev = items[i - 1][1] if i > 0 else None
        nxt = items[i + 1][1] if i + 1 < len(items) else None
        by3[(txt, prev, nxt)].append(i)
        by_prev[(txt, prev)].append(i)
        by_next[(txt, nxt)].append(i)
        by_en[txt].append(i)
    return by3, by_prev, by_next, by_en


def resolve(anchor, idx):
    """Capayi hedef exe'deki konum listesine cevir. (konumlar, yontem) dondurur."""
    by3, by_prev, by_next, by_en = idx
    en, prev, nxt = anchor['en'], anchor.get('prev'), anchor.get('next')
    hit = by3.get((en, prev, nxt))
    if hit:
        return hit, 'tam'
    hit = by_prev.get((en, prev))
    if hit:
        return hit, 'onceki'
    hit = by_next.get((en, nxt))
    if hit:
        return hit, 'sonraki'
    hit = by_en.get(en)
    if hit and len(hit) == 1:
        return hit, 'tekil-metin'
    if hit:
        return [], 'belirsiz(%d aday)' % len(hit)
    return [], 'yok'


def run(ascii_mode=True, report_only=False, src=None, dst=None):
    src = src or ORIG
    dst = dst or EXE
    if not os.path.exists(src):
        print('KAYNAK YOK: %s' % src)
        print('Ipucu: once orijinal exe yedeklenmelidir (Exanima.exe.orijinal).')
        return 1

    anchors = json.load(io.open(ANCHORS, encoding='utf-8'))
    data = bytearray(open(src, 'rb').read())
    items = scan(data)
    idx = build_index(items)

    applied, toolong, unmatched = [], [], []
    touched = set()
    methods = defaultdict(int)

    for a in anchors:
        spots, how = resolve(a, idx)
        methods[how] += 1
        if not spots:
            unmatched.append((a['en'], a['tr'], how))
            continue
        # Gravur stilindeki ekranlar (ana menu, karakter unvanlari) harf disinda
        # HICBIR sey cizmiyor - noktalama dahil. Sadece onlar ASCII kalir.
        plain = ascii_mode or a['en'] in STYLIZED
        text = a['tr'].translate(TRMAP) if plain else a['tr']
        try:
            nb = text.encode('ascii' if plain else 'cp1254')
        except UnicodeEncodeError:
            toolong.append((a['en'], text, 'kodlanamadi'))
            continue
        for i in spots:
            off, eng, cap = items[i]
            if len(nb) > cap:
                toolong.append((eng, text, '%d > tampon %d' % (len(nb), cap)))
                continue
            if not report_only:
                struct.pack_into('<Q', data, off - 8, len(nb))
                data[off:off + cap + 1] = nb + bytes(cap + 1 - len(nb))
            touched.add(off)
            applied.append((off, eng, text))

    print('=== ESLESME YONTEMLERI ===')
    for k in ('tam', 'onceki', 'sonraki', 'tekil-metin'):
        if methods.get(k):
            print('  %-12s %d' % (k, methods[k]))
    for k, v in methods.items():
        if k.startswith('belirsiz') or k == 'yok':
            print('  %-12s %d' % (k, v))

    if toolong:
        print('\n!!! TAMPONA SIGMAYAN (%d) - Ingilizce kalir:' % len(toolong))
        for eng, tr, why in toolong[:40]:
            print('  %-32s -> %-32s [%s]' % (eng[:32], tr[:32], why))

    if unmatched:
        print('\n!!! ESLESMEYEN (%d) - oyun bu metinleri degistirmis olabilir:' % len(unmatched))
        for eng, tr, how in unmatched[:40]:
            print('  %-40s (%s)' % (eng[:40], how))

    if report_only:
        print('\n=== YENI / CEVRILMEMIS METINLER ===')
        known = {a['en'] for a in anchors}
        fresh = [(o, t) for o, t, c in items
                 if o not in touched and t not in known and len(t) > 3
                 and not re.match(r'^(sysconst\.|rtlconsts\.|SteamAPI|Msc_|WH_)', t)
                 and not GLSL.search(t)]
        print('  aday: %d' % len(fresh))
        for o, t in fresh[:60]:
            print('    %06X  %s' % (o, t[:80]))
    else:
        open(dst, 'wb').write(bytes(data))

    print('\nOZET: %d uygulandi | %d sigmadi | %d eslesmedi | mod=%s'
          % (len(applied), len(toolong), len(unmatched), 'ASCII' if ascii_mode else 'TAM TURKCE'))
    return 0


if __name__ == '__main__':
    run(ascii_mode='--turkce' not in sys.argv,
        report_only='--rapor' in sys.argv)
