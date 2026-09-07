# -*- coding: utf-8 -*-
"""Exanima font ilerleme-genisligi (advance) tablosu yamasi.

SORUN:
  Turkce harfleri Latin-5 kod noktalarina cizdik: I->0xDD (CP1252'de Y-akut),
  i->0xFD (y-akut), S->0xDE (thorn), s->0xFE, G->0xD0 (eth), g->0xF0.
  Oyun harf genisligini atlastaki mureekkepten OLCMUYOR; exe icinde her font
  icin 256 girisli int16 bir "advance delta" tablosu tutuyor. Yani 0xDD hala
  Y'nin genisligiyle ilerliyor -> "ILERI" yerine "I  LERI" gibi bosluk.

COZUM:
  Her tabloda Turkce kod noktalarina, harfin turedigi ASCII harfin degerini
  yaz. Ornek: t[0xDD] = t[0x49] ('I'), t[0xFD] = t[0x69] ('i').

TABLOYU BULMA (surumden bagimsiz):
  Tablo adresini sabit yazmak guncellemede coker. Bunun yerine exe'deki tum
  int16 dizileri taranir ve ASCII araliginin (0x21..0x7E) fontbase24r'deki
  gercek mureekkep genisliklerine KORELASYONU olculur. r > 0.60 olan konumlar
  font tablolaridir (oyunda 6 font -> 6 tablo).
"""
import array
import sys

# fontbase24r atlasindan olculen ASCII mureekkep genislikleri (0x21..0x7E).
# Tablolar bunun yaklasik yarisi kadar bir delta tutar; korelasyon icin yeterli.
REF = [6, 12, 22, 18, 36, 26, 4, 9, 9, 15, 23, 8, 12, 6, 16, 22, 11, 20, 19, 22,
       19, 20, 20, 20, 21, 6, 8, 21, 23, 21, 12, 31, 29, 21, 27, 27, 17, 17, 29,
       27, 5, 10, 23, 18, 33, 26, 34, 20, 34, 23, 19, 24, 26, 28, 37, 24, 25, 26,
       8, 20, 8, 22, 22, 10, 20, 21, 20, 21, 20, 14, 20, 18, 5, 10, 19, 4, 31, 18,
       22, 21, 21, 11, 15, 12, 19, 20, 33, 20, 21, 20, 10, 4, 10, 22]

# Turkce kod noktasi -> genisligini miras alacagi ASCII harf
MIRAS = {
    # Latin-5'e ciziler harfler (CP1252'de baska harflerin yerinde durur)
    0xDD: 0x49,   # I noktali      <- I
    0xFD: 0x69,   # i noktasiz     <- i
    0xDE: 0x53,   # S cedilli      <- S
    0xFE: 0x73,   # s cedilli      <- s
    0xD0: 0x47,   # G yumusak      <- G
    0xF0: 0x67,   # g yumusak      <- g
    # CP1252'de ZATEN bulunan harfler: ilk uc fontta advance degeri 0 kalmis
    # (orijinal oyun bunlari hic kullanmiyordu), bu yuzden harf olmasi
    # gerekenden dar ilerliyor ve saginda kalan harf ustune biniyordu.
    0xC7: 0x43,   # C cedilli      <- C
    0xE7: 0x63,   # c cedilli      <- c
    0xD6: 0x4F,   # O umlautlu     <- O
    0xF6: 0x6F,   # o umlautlu     <- o
    0xDC: 0x55,   # U umlautlu     <- U
    0xFC: 0x75,   # u umlautlu     <- u
    # duzeltme isaretli harfler (kagit, hala, kar vb.)
    0xC2: 0x41,   # A duzeltmeli   <- A
    0xE2: 0x61,   # a duzeltmeli   <- a
    0xCE: 0x49,   # I duzeltmeli   <- I
    0xEE: 0x69,   # i duzeltmeli   <- i
    0xDB: 0x55,   # U duzeltmeli   <- U
    0xFB: 0x75,   # u duzeltmeli   <- u
}


def tablolari_bul(raw, esik=0.60):
    """exe baytlarinda font advance tablolarinin bayt ofsetlerini dondurur.

    ON ELEME
      Tablolarda kontrol karakterleri (0x0A..0x1F) hep 0. Bu 22 int16'lik sifir
      kosusu bytes.find ile C hizinda taranir; korelasyon yalnizca hayatta kalan
      birkac bin adaya uygulanir. Boylece numpy'a gerek kalmaz.
    """
    t = array.array('h')
    t.frombytes(raw[:len(raw) // 2 * 2])
    ort_r = sum(REF) / len(REF)
    sap_r = (sum((x - ort_r) ** 2 for x in REF) / len(REF)) ** 0.5
    refn = [(x - ort_r) / sap_r for x in REF]

    KOSU = bytes(22 * 2)          # t[0x0A..0x20) hepsi sifir
    bulunan, onceki, p = [], -99, -1
    while True:
        p = raw.find(KOSU, p + 1)
        if p < 0:
            break
        if p % 2:
            continue
        off = p - 0x0A * 2        # tablo basi
        if off < 0 or off + 512 > len(raw) or off - onceki < 64:
            continue
        i = off // 2
        if any(t[i + c] for c in range(1, 9)):
            continue
        dilim = t[i + 0x21:i + 0x7F]
        if len(set(dilim)) < 6 or max(dilim) - min(dilim) < 4:
            continue
        ort = sum(dilim) / len(dilim)
        sap = (sum((x - ort) ** 2 for x in dilim) / len(dilim)) ** 0.5
        if sap < 1e-9:
            continue
        r = sum((x - ort) / sap * y for x, y in zip(dilim, refn)) / len(dilim)
        if r > esik:
            onceki = off
            bulunan.append((off, r))
    return bulunan


def yamala(data, sessiz=False):
    """data: bytearray (exe). Yerinde degistirir, yamalanan tablo sayisini doner."""
    tablolar = tablolari_bul(bytes(data))
    if not sessiz:
        print('  advance tablosu bulundu: %d' % len(tablolar))
    n = 0
    for off, r in tablolar:
        t = array.array('h')
        t.frombytes(bytes(data[off:off + 512]))
        for hedef, kaynak in MIRAS.items():
            t[hedef] = t[kaynak]
        data[off:off + 512] = t.tobytes()
        n += 1
        if not sessiz:
            print('    0x%06X (r=%.2f)  I=%-3d i=%-3d S=%-3d s=%-3d G=%-3d g=%-3d '
                  'C=%-3d O=%-3d U=%-3d o=%-3d u=%d'
                  % (off, r, t[0xDD], t[0xFD], t[0xDE], t[0xFE], t[0xD0], t[0xF0],
                     t[0xC7], t[0xD6], t[0xDC], t[0xF6], t[0xFC]))
    return n


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    yol = r'E:\Steam\steamapps\common\Exanima\Exanima.exe'
    d = bytearray(open(yol, 'rb').read())
    print('%d tablo yamalandi' % yamala(d))
    open(yol, 'wb').write(bytes(d))
