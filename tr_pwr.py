# -*- coding: utf-8 -*-
"""Exanima .pwr (guc agaci) dosyalarinin metin tablosunu yeniden yazar.

BICIM
  ... dugum verisi ...
  [ofset tablosu]   N+1 adet u32; her biri metin tablosunun BASINA gore ofset,
                    sonuncusu dosya sonu (sinir). Bazi girisler -1 veya baska
                    bir sayi olabilir (kullanilmayan/olu dugumler).
  [metin tablosu]   arka arkaya [u32 uzunluk][ASCII veri], dosya sonuna kadar.

Ceviri metinleri uzunlugu degistirdigi icin ofset tablosu da guncellenmeli.
GUVENLIK: sadece metin tablosunun HEMEN oncesindeki N+1 slotluk pencereye
dokunulur ve orada yalnizca degeri gecerli bir metin basi olan slotlar
yazilir. Boylece -1 gibi nobetciler ve dugum alanlari korunur.
"""
import struct

# CP1254 Turkce harfleri 0x80-0xFF araliginda; yamali dosyalari da
# okuyabilmek icin bu araligi da kabul ediyoruz.
YAZDIRILABILIR = set(range(32, 127)) | set(range(0x80, 0x100)) | {9, 10, 13}


def coz(b):
    """-> (tablo_basi, [(goreli_ofset, metin), ...])  bulunamazsa None"""
    for start in range(0x40, len(b) - 8):
        p, cnt = start, 0
        while p < len(b) - 4:
            n = struct.unpack('<I', b[p:p + 4])[0]
            if not (0 <= n <= 400 and p + 4 + n <= len(b)):
                break
            if not all(c in YAZDIRILABILIR for c in b[p + 4:p + 4 + n]):
                break
            cnt += 1
            p += 4 + n
        if p == len(b) and cnt >= 20:
            r, p = [], start
            while p < len(b):
                n = struct.unpack('<I', b[p:p + 4])[0]
                r.append((p - start, b[p + 4:p + 4 + n].decode('latin-1')))
                p += 4 + n
            return start, r
    return None


def _pencere(b, start, gecerli):
    """Ofset tablosunun basini geriye yuruyerek bulur.

    Tablo metin tablosunun hemen oncesinde biter. Icinde -1 gibi nobetciler ve
    kucuk sayilar bulunabilir; ust uste 5 gecersiz slot gorunce dururuz. Bu
    sinir, dugum verisindeki float'lara (u32 olarak cok buyuk sayilar) carpar.
    """
    i, bosluk, ilk = start - 4, 0, start
    while i >= 0:
        v = struct.unpack('<I', b[i:i + 4])[0]
        if v in gecerli:
            bosluk, ilk = 0, i
        elif v > 0xF0000000 or v < 0x10000:      # -1 / kucuk alanlar: tolere et
            bosluk += 1
        else:                                    # float ya da isaretci: tablo bitti
            bosluk = 99
        if bosluk >= 5:
            break
        i -= 4
    return ilk


def yaz(b, ceviri, kodlama='cp1254'):
    """ceviri: {ingilizce: turkce}. Yeni dosya baytlarini dondurur."""
    start, metinler = coz(b)
    n = len(metinler)

    yeni_govde = bytearray()
    esle = {}                                   # eski goreli ofset -> yeni
    for eski_off, metin in metinler:
        yeni = ceviri.get(metin, metin)
        try:
            ham = yeni.encode(kodlama)
        except UnicodeEncodeError:
            ham = metin.encode('latin-1')
        esle[eski_off] = len(yeni_govde)
        yeni_govde += struct.pack('<I', len(ham)) + ham
    esle[len(b) - start] = len(yeni_govde)      # sinir nobetcisi

    bas = bytearray(b[:start])
    pencere = _pencere(b, start, set(esle))
    degisen = 0
    for i in range(max(0, pencere), start, 4):
        v = struct.unpack('<I', bas[i:i + 4])[0]
        if v in esle:
            struct.pack_into('<I', bas, i, esle[v])
            degisen += 1
    return bytes(bas) + bytes(yeni_govde), degisen, n


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    for fn in ('pwr_mind.pwr', 'pwr_force.pwr', 'pwr_energy.pwr', 'pwr_displace.pwr'):
        d = open('ext2/' + fn, 'rb').read()
        out, deg, n = yaz(d, {}, 'latin-1')
        print('%-17s metin=%-3d yazilan ofset=%-3d  kimlik testi: %s'
              % (fn, n, deg, 'GECTI' if out == d else 'KALDI'))
