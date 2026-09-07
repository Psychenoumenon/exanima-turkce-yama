# -*- coding: utf-8 -*-
"""Exanima Turkce Yama - tek komutluk uygulayici.

    python uygula.py

Sirasiyla:
  1) Exanima.exe.orijinal -> Exanima.exe  (925 capa, CP1254 tam Turkce)
  2) exe icine gomulu 5 fontu Turkce glifli surumleriyle degistirir
  3) 6 font advance (harf genisligi) tablosunda Turkce kod noktalarini duzeltir
  3b) guc carkinin alan adlari (16 baytlik C dizisi tablosu)
  4) Resource.rpk'yi yeniden kurar:
       fontbase24r      Turkce glifli font atlasi
       objstrings.rdb   esya adlari ve aciklamalari
       pwr_*.pwr        guc agaci adlari ve ipuclari
       charroles.rdb    NPC diyaloglari
       narrator.rcd     anlatici
       exanima*.rfc     dunyadaki kitap, gunluk, mektup ve notlar
       manual*.fds      oyun ici kilavuz (12 bolum x 2 surum)

Her adim ORIJINAL yedekten okur; tekrar tekrar calistirmak guvenlidir.
Oyun guncellenirse once yedekleri tazele:
    Exanima.exe -> Exanima.exe.orijinal , Resource.rpk -> Resource.rpk.orijinal
sonra `python tr_patch2.py --rapor` ile degisen metinleri listele.
"""
import hashlib
import io
import json
import os
import pickle
import struct
import sys

import charroles_tr
import manual_tr
import pwr_tr
import rfc_tr
import rfi_codec
import tr_patch2
import tr_charroles
import tr_pwr
import tr_rdb
import tr_rfc
import tr_widths

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HERE = tr_patch2.kaynak_kok()

OYUN = EXE = EXE_ORIJ = RPK = RPK_ORIJ = None


def yolu_ayarla(oyun):
    """Oyun klasorunu belirler; tr_patch2'yi de birlikte ayarlar."""
    global OYUN, EXE, EXE_ORIJ, RPK, RPK_ORIJ
    OYUN = oyun
    EXE = os.path.join(OYUN, 'Exanima.exe')
    EXE_ORIJ = EXE + '.orijinal'
    RPK = os.path.join(OYUN, 'Resource.rpk')
    RPK_ORIJ = RPK + '.orijinal'
    tr_patch2.yolu_ayarla(oyun)


yolu_ayarla(r'E:\Steam\steamapps\common\Exanima')

MAGIC = struct.pack('<I', rfi_codec.MAGIC)


def rfi_uzunluk(body, nchan, expected):
    """RLE akisinin KAC BAYT tuketildigi. Gomulu blobun sinirini bulmak icin."""
    rb = rfi_codec.runbase(nchan)
    i = n = 0
    while n < expected:
        c = body[i]
        i += 1
        if c < rb:
            k = (c + 1) * nchan
            n += k
            i += k
        else:
            n += (c - 61) * nchan
            i += nchan
    return i


def gomulu_fontlar(raw):
    """exe icindeki .rfi bloblarini bul -> [(offset, uzunluk, w, h, nchan)]"""
    out, p = [], -1
    while True:
        p = raw.find(MAGIC, p + 1)
        if p < 0:
            return out
        try:
            h = struct.unpack('<8I', raw[p:p + 32])
        except struct.error:
            return out
        w, ht, fmt, store, dsz = h[1], h[2], h[4], h[6], h[7]
        nch = rfi_codec.NCHAN.get(fmt)
        if nch is None or not (0 < w <= 4096) or not (0 < ht <= 4096):
            continue
        try:
            L = 32 + (rfi_uzunluk(raw[p + 32:], nch, dsz) if store == rfi_codec.RLE else dsz)
        except (IndexError, ValueError):
            continue
        out.append((p, L, w, ht, nch))


def fontlari_yamala(data, orij):
    """Gomulu fontlari hash ile eslestirip yerinde degistirir."""
    tablo = pickle.load(open(os.path.join(HERE, 'exefonts_TR_hash.pkl'), 'rb'))
    n = 0
    for off, L, w, ht, nch in gomulu_fontlar(orij):
        h = hashlib.sha1(orij[off:off + L]).hexdigest()
        if h not in tablo:
            continue
        _, _, _, _, yeni = tablo[h]
        if len(yeni) > L:
            print('    0x%06X %dx%d ATLANDI (%d > %d bayt)' % (off, w, ht, len(yeni), L))
            continue
        # RLE cozucu hedef piksel sayisina ulasinca durur; artan baytlar okunmaz.
        data[off:off + len(yeni)] = yeni
        n += 1
        print('    0x%06X %4dx%-4d  %d -> %d bayt' % (off, w, ht, L, len(yeni)))
    return n


# ------------------------------------------------- guc agaci alan adlari
# Guc carkinin (TDomainWheel) alan basliklari Delphi sabiti degil, 16 bayta
# hizalanmis duz C dizileri: bu yuzden metin yamalayicisi bunlari hic gormedi
# ve carkta "Force" gibi Ingilizce kaliyordu. Tablo, icerigiyle aranir.
ALAN_ADLARI = [('Mind', 'Zihin'), ('Force', 'Kuvvet'), ('Body', 'Beden'),
               ('Energy', 'Enerji'), ('Light', 'Işık'),
               ('Displacement', 'Yer Değiştirme')]
ALAN_SLOT = 16


def _alan_imzasi():
    return b''.join(en.encode() + bytes(ALAN_SLOT - len(en)) for en, _ in ALAN_ADLARI)


def alanlari_yamala(data):
    p = bytes(data).find(_alan_imzasi())
    if p < 0:
        print('    tablo bulunamadi - alan adlari Ingilizce kalacak')
        return 0
    for i, (en, tr) in enumerate(ALAN_ADLARI):
        ham = tr.encode('cp1254')
        if len(ham) >= ALAN_SLOT:
            print('    %s sigmadi (%d >= %d)' % (tr, len(ham), ALAN_SLOT))
            continue
        data[p + i * ALAN_SLOT: p + (i + 1) * ALAN_SLOT] = ham + bytes(ALAN_SLOT - len(ham))
    print('    0x%06X  %s' % (p, ', '.join('%s->%s' % x for x in ALAN_ADLARI)))
    return len(ALAN_ADLARI)


# ---------------------------------------------------------------- RPK
def rpk_oku(yol):
    d = open(yol, 'rb').read()
    idx_size = struct.unpack('<I', d[4:8])[0]
    kayit = []
    for i in range(8, 8 + idx_size, 32):
        ad = d[i:i + 16].rstrip(b'\x00').decode('latin-1')
        off, size = struct.unpack('<II', d[i + 16:i + 24])
        kayit.append([ad, off, size, d[i + 24:i + 32]])
    return d, idx_size, kayit


# Kilavuzun SOL MENUSUNDEKI bolum secenekleri .fds indeksindeki 16 baytlik
# giris adlaridir - bolum metninin icinde degil. Bu yuzden bolum metinleri
# Turkce olmasina ragmen menude 'movement', 'inventory' gibi Ingilizce kaliyordu.
# Bu adlar ne exe'de ne de baska bir arsiv girisinde referans ediliyor
# (thaumaturgy / encounters / interaction / shields / saving: 0 gecis),
# yani yalnizca bu menude gorunuyorlar; guvenle degistirilebilirler.
KILAVUZ_BOLUM_ADLARI = {
    'armour': 'zırh',
    'combat': 'dövüş',
    'encounters': 'karşılaşmalar',
    'health': 'sağlık',
    'interaction': 'etkileşim',
    'inventory': 'envanter',
    'movement': 'hareket',
    'saving': 'kayıt',
    'shields': 'kalkanlar',
    'skills': 'yetenekler',
    'thaumaturgy': 'tömaturji',
    'weapons': 'silahlar',
}
AD_SLOT = 16


def rpk_kur(ham, degisim, ad_degisim=None):
    """Bellekte RPK bicimli bir arsivi yeniden kurar (kilavuz .fds icin de gecerli).

    ad_degisim: {eski_giris_adi: yeni_giris_adi} - indeksteki 16 baytlik ad
    alanini da yeniden yazar. Giris sirasi korunur.
    """
    ad_degisim = ad_degisim or {}
    idx_size = struct.unpack('<I', ham[4:8])[0]
    veri_bas = 8 + idx_size
    yeni_idx, govde = bytearray(), bytearray()
    for i in range(8, 8 + idx_size, 32):
        ad = ham[i:i + AD_SLOT].rstrip(b'\x00').decode('latin-1')
        off, size = struct.unpack('<II', ham[i + 16:i + 24])
        icerik = degisim.get(ad) or ham[veri_bas + off: veri_bas + off + size]
        yazilacak = ad_degisim.get(ad, ad).encode('cp1254')
        if len(yazilacak) > AD_SLOT:
            print('    giris adi sigmadi, Ingilizce kaldi: %s' % ad)
            yazilacak = ad.encode('latin-1')
        yeni_idx += yazilacak.ljust(AD_SLOT, b'\x00')
        yeni_idx += struct.pack('<II', len(govde), len(icerik))
        yeni_idx += ham[i + 24:i + 32]
        govde += icerik
    return ham[:4] + struct.pack('<I', len(yeni_idx)) + bytes(yeni_idx) + bytes(govde)


def kilavuz_kur(ham, bolumler):
    """bolumler: {bolum_adi: turkce_metin}. Satir sonlari CRLF'e cevrilir."""
    degisim = {ad: metin.replace('\r\n', '\n').replace('\n', '\r\n').encode('cp1254')
               for ad, metin in bolumler.items()}
    return rpk_kur(ham, degisim, KILAVUZ_BOLUM_ADLARI)


def rpk_yaz(kaynak, hedef, degisim):
    """degisim: {dosya_adi: yeni_bayt}. Arsivi bastan kurar."""
    d, idx_size, kayit = rpk_oku(kaynak)
    veri_bas = 8 + idx_size
    yeni_idx = bytearray()
    govde = bytearray()
    for ad, off, size, kuyruk in kayit:
        icerik = degisim.get(ad) or d[veri_bas + off: veri_bas + off + size]
        yeni_idx += ad.encode('latin-1').ljust(16, b'\x00')
        yeni_idx += struct.pack('<II', len(govde), len(icerik))
        yeni_idx += kuyruk
        govde += icerik
    with open(hedef, 'wb') as f:
        f.write(d[:4] + struct.pack('<I', len(yeni_idx)) + bytes(yeni_idx) + bytes(govde))
    return len(kayit)


def main(oyun=None):
    if oyun:
        yolu_ayarla(oyun)
    for p in (EXE_ORIJ, RPK_ORIJ):
        if not os.path.exists(p):
            print('YEDEK YOK: %s' % p)
            return 1

    print('[1/4] Metinler (CP1254 tam Turkce)')
    if tr_patch2.run(ascii_mode=False):
        return 1

    orij = open(EXE_ORIJ, 'rb').read()
    data = bytearray(open(EXE, 'rb').read())

    print('\n[2/4] exe icindeki fontlar')
    print('    %d font degistirildi' % fontlari_yamala(data, orij))

    print('\n[3/4] Harf genisligi (advance) tablolari')
    tr_widths.yamala(data)

    print('\n[3b] Guc agaci alan adlari')
    alanlari_yamala(data)

    open(EXE, 'wb').write(bytes(data))

    print('\n[4/4] Resource.rpk')
    _, idx0, kayit0 = rpk_oku(RPK_ORIJ)
    ham = open(RPK_ORIJ, 'rb').read()
    veri = 8 + idx0
    icerik = {ad: ham[veri + o:veri + o + s] for ad, o, s, _ in kayit0}

    degisim = {'fontbase24r': open(os.path.join(HERE, 'fontbase24r_TR2.rfi'), 'rb').read()}
    print('    fontbase24r  Turkce glifli surum')

    # Esya adlari ve aciklamalari (objstrings.rdb)
    obj = {d['en']: d['tr'] for d in json.load(io.open(os.path.join(HERE, 'obj_tr.json'),
                                                      encoding='utf-8'))}
    degisim['objstrings.rdb'] = tr_rdb.yaz(icerik['objstrings.rdb'], obj)
    print('    objstrings.rdb  %d esya metni' % len(obj))

    # Guc agaci adlari ve ipuclari (pwr_*.pwr)
    for ad in sorted(a for a in icerik if a.endswith('.pwr')):
        yeni, kac, n = tr_pwr.yaz(icerik[ad], pwr_tr.TR)
        degisim[ad] = yeni
        print('    %-17s %d metin, %d ofset guncellendi' % (ad, n, kac))

    # NPC diyaloglari - SABIT UZUNLUK (bkz. tr_charroles.blob_yaz)
    sig_rol = []
    degisim['charroles.rdb'], kac, adet = tr_charroles.yaz(icerik['charroles.rdb'],
                                                           charroles_tr.TR,
                                                           sigmayan=sig_rol)
    assert len(degisim['charroles.rdb']) == len(icerik['charroles.rdb']),         'charroles.rdb boyu degisti - ic boyut alanlari bozulur'
    print('    charroles.rdb     %d kayit, %d diyalog satiri%s'
          % (adet, kac, ', %d SIGMADI' % len(sig_rol) if sig_rol else ''))

    # Anlatici - SABIT UZUNLUK
    sig_anl = []
    degisim['narrator.rcd'], kac = tr_charroles.duz_yaz(icerik['narrator.rcd'],
                                                        charroles_tr.NARRATOR,
                                                        sigmayan=sig_anl)
    assert len(degisim['narrator.rcd']) == len(icerik['narrator.rcd'])
    print('    narrator.rcd      %d metin%s'
          % (kac, ', %d SIGMADI' % len(sig_anl) if sig_anl else ''))

    # Dunyadaki kitap, gunluk, mektup ve notlar (.rfc icine gomulu RDB'ler)
    n_rfc = n_metin = 0
    for ad in sorted(a for a in icerik if a.endswith('.rfc')):
        if not tr_rfc.gomulu_rdb(icerik[ad]):
            continue
        yeni, kac, sigmayan = tr_rfc.yaz(icerik[ad], rfc_tr.TR,
                                          yerinde=rfc_tr.YERINDE.get(ad))
        if sigmayan:
            print('    %-17s %d gomulu RDB sigmadi - Ingilizce kaldi' % (ad, sigmayan))
        degisim[ad] = yeni
        n_rfc += 1
        n_metin += kac
    print('    %d seviye dosyasi, %d kitap/gunluk metni' % (n_rfc, n_metin))

    # Oyun ici kilavuz (klavye ve oyun kolu surumleri)
    for ad, bolumler in manual_tr.METIN.items():
        degisim[ad] = kilavuz_kur(icerik[ad], bolumler)
        print('    %-17s %d bolum (menu adlari da Turkce)' % (ad, len(bolumler)))

    n = rpk_yaz(RPK_ORIJ, RPK, degisim)
    print('    %d kayit yeniden yazildi (%.1f MB)' % (n, os.path.getsize(RPK) / 1e6))

    print('\nTAMAM.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
