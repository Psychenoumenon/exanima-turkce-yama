# -*- coding: utf-8 -*-
"""Seviye dosyalarina (.rfc) gomulu kitap / gunluk / mektup metinleri.

BULGU
  Dunyada okunan kitap ve gunlukler objstrings.rdb'de DEGIL, her seviyenin kendi
  .rfc dosyasinin ICINE gomulu ayri bir RDB'de duruyor (magic 02 0c bf af).
  Yapisi objstrings.rdb ile birebir ayni: 16 baytlik [a][f][offset][length]
  indeksi, ardindan metin havuzu.

NEDEN HAVUZ DOLDURULUYOR
  .rfc bir sahne dosyasi; icinde baska ofsetler olup olmadigini bilmiyoruz.
  Bu yuzden gomulu RDB'nin TOPLAM BOYUTU degistirilmez: yeni havuz orijinal
  havuz boyutuna sifirla tamamlanir. Boylece .rfc'nin uzunlugu ve gomulu RDB'den
  sonraki her bayt oldugu yerde kalir - sifir risk.
  Ceviri havuza sigmazsa o dosya Ingilizce birakilir ve raporlanir.
"""
import re
import struct

import tr_rdb

MAGIC = b'\x02\x0c\xbf\xaf'


def gomulu_rdb(blob, en_az_metin=1):
    """-> [(rdb_offset, index_size, havuz_boyutu)] - metin tasiyan gomulu RDB'ler."""
    out = []
    for p in (m.start() for m in re.finditer(re.escape(MAGIC), blob)):
        idx = struct.unpack('<I', blob[p + 4:p + 8])[0]
        if idx == 0 or idx % 16 or idx > 200000 or p + 8 + idx > len(blob):
            continue
        veri = p + 8 + idx
        son, nesir = 0, 0
        for i in range(idx // 16):
            _, _, o, l = struct.unpack('<4I', blob[p + 8 + i * 16:p + 8 + i * 16 + 16])
            if l > 20000 or veri + o + l > len(blob):
                continue
            son = max(son, o + l)
            if l > 20:
                nesir += 1
        if nesir >= en_az_metin and son:
            out.append((p, idx, son))
    return out


def yerinde_yaz(out, ceviri, kodlama='cp1254'):
    """Indeks disi metinleri AYNI UZUNLUKTA yerinde degistirir (bosluk dolgulu)."""
    n = 0
    for en, tr in ceviri.items():
        ham_en = en.encode('latin-1')
        p = bytes(out).find(ham_en)
        if p < 0:
            continue
        ham_tr = tr.encode(kodlama)
        if len(ham_tr) > len(ham_en):
            continue
        out[p:p + len(ham_en)] = ham_tr + b' ' * (len(ham_en) - len(ham_tr))
        n += 1
    return n


def yaz(blob, ceviri, kodlama='cp1254', yerinde=None):
    """-> (yeni_blob, degisen_metin_sayisi, sigmayan_rdb_sayisi)"""
    out = bytearray(blob)
    degisen = sigmayan = 0
    for p, idx, havuz in gomulu_rdb(blob):
        eski = bytes(blob[p:p + 8 + idx + havuz])
        yeni = tr_rdb.yaz(eski, ceviri, kodlama)
        if len(yeni) > len(eski):
            sigmayan += 1
            continue
        _, kayitlar = tr_rdb.oku(eski)
        degisen += sum(1 for _, _, t in kayitlar if t in ceviri)
        out[p:p + len(eski)] = yeni + bytes(len(eski) - len(yeni))
    if yerinde:
        degisen += yerinde_yaz(out, yerinde, kodlama)
    return bytes(out), degisen, sigmayan


if __name__ == '__main__':
    import sys
    import uygula
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    G = r'E:\Steam\steamapps\common\Exanima'
    raw, i0, kayit = uygula.rpk_oku(G + r'\Resource.rpk.orijinal')
    base = 8 + i0
    tamam = True
    for ad, o, s, _ in kayit:
        if not ad.endswith('.rfc'):
            continue
        b = raw[base + o:base + o + s]
        if not gomulu_rdb(b):
            continue
        aynen, _, _ = yaz(b, {}, 'latin-1')
        ok = aynen == b
        tamam &= ok
        print('%-18s %s' % (ad, 'GECTI' if ok else 'KALDI'))
    print('kimlik testi:', 'TUMU GECTI' if tamam else 'HATA VAR')
