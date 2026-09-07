# -*- coding: utf-8 -*-
"""charroles.rdb yeniden yazicisi (NPC diyaloglari).

BICIM
  RDB: 16 baytlik indeks kayitlari [a][f][offset][length], ardindan blob havuzu.
  Her blob bir "rol" tanimi: 4 bayt KENDI UZUNLUGU, 4 bayt bayrak, 16 baytlik ad
  alani, sonra dugum verisi. Diyalog satirlari ve betik kodu blob'un ICINE
  [u32 uzunluk][ASCII] biciminde gomulu; ayri bir metin tablosu yok.

NEDEN UZUNLUK DEGISTIREBILIYORUZ
  Kayit ici mutlak ofset yok: tum blob'lar tarandiginda, blob uzunlugunu tasiyan
  tek u32 blob[0]. (Metin konumlarina esit u32 orani %1.4, yani rastlanti
  duzeyinde.) Bu yuzden yalnizca blob[0] ve RDB indeksi guncellenir.

BETIK REFERANSLARI  (bkz. _betik_duzelt)
  Diyalog konulari betiklerden GORUNEN METINLERIYLE cagriliyor. Konuyu cevirip
  cagriyi cevirmezsek oyun konuyu bulamiyor ve her karede
  "Error evaluating local characters: <ad>" hatasi basiyor.

GUVENLIK
  Yalnizca ceviri tablosunda BIREBIR karsiligi olan diziler ve yukaridaki betik
  cagrilari degistirilir; geri kalan her bayt aynen kopyalanir.
"""
import re
import struct

YAZDIRILABILIR = set(range(32, 127)) | set(range(0x80, 0x100)) | {9, 10, 13}

_CAGRI = re.compile(r'([A-Za-z_][A-Za-z0-9_]*)\(([^()]*)\)')


def _betik_mi(metin):
    """Fonksiyon cagrisi tasiyan betik dizisi mi?"""
    s = metin.rstrip()
    return '(' in s and s.endswith((';', ')'))


def _betik_duzelt(metin, ceviri, kodlama=None):
    """Betikteki konu adlarini ceviriyle ayni tutar.

        result = (TopicUsed(Who are you?) = 0);
    ->  result = (TopicUsed(Sen kimsin?) = 0);

    Yalnizca bir argumanin TAMAMI ceviri tablosunda anahtar ise degistirilir;
    ayrac ve bosluklar oldugu gibi korunur.
    """
    if not _betik_mi(metin):
        return metin

    def _arg(m):
        parcalar, degisti = [], False
        for p in m.group(2).split(','):
            ic = p.strip()
            yeni = ceviri.get(ic)
            if ic and yeni and not set('(),').intersection(yeni):
                if kodlama:
                    yeni = _doldur(yeni, len(ic.encode('latin-1')), kodlama)
                    if yeni is None:
                        parcalar.append(p)
                        continue
                parcalar.append(p.replace(ic, yeni, 1))
                degisti = True
            else:
                parcalar.append(p)
        return '%s(%s)' % (m.group(1), ','.join(parcalar)) if degisti else m.group(0)

    return _CAGRI.sub(_arg, metin)


def _dizi(blob, p):
    """p konumunda [u32 uzunluk][ASCII] varsa (uzunluk, metin) doner."""
    if p + 4 > len(blob):
        return None
    n = struct.unpack('<I', blob[p:p + 4])[0]
    if not (2 <= n <= 400 and p + 4 + n <= len(blob)):
        return None
    s = blob[p + 4:p + 4 + n]
    if not all(c in YAZDIRILABILIR for c in s):
        return None
    return n, s.decode('latin-1')


def _doldur(metin, hedef, kodlama):
    """metin'i tam `hedef` bayta bosluk ile doldurur; sigmazsa None."""
    ham = metin.encode(kodlama)
    if len(ham) > hedef:
        return None
    return metin + ' ' * (hedef - len(ham))


def blob_yaz(blob, ceviri, kodlama='cp1254', sabit=True, sigmayan=None):
    """Blob'u yeniden kurar. -> (yeni_blob, degisen_sayisi)

    sabit=True (VARSAYILAN):
      Her dizi ORIJINAL BAYT UZUNLUGUNU korur; kisa ceviriler sona bosluk ile
      doldurulur, sigmayanlar Ingilizce birakilir ve `sigmayan` listesine yazilir.

      NEDEN: rol blob'unun icinde ic ice gecmis KAPSAYICI BOYUT ALANLARI var
      (ornegin 0x38'deki u32 icin 56 + deger == blob uzunlugu; 49 blob'un
      12'sinde gecerli). Uzunluk degistiginde bunlar bozuluyor ve oyunun YZ'si
      her karede "Error evaluating local characters: <ad>" hatasi veriyor.
      Uzunlugu sabit tutunca tek bir bayt bile yer degistirmiyor: blob boyu,
      butun ic boyut alanlari ve RDB indeksi aynen gecerli kaliyor."""
    out = bytearray()
    p = 0
    degisen = 0
    while p < len(blob):
        d = _dizi(blob, p)
        if d is None:
            out.append(blob[p])
            p += 1
            continue
        n, metin = d
        yeni = ceviri.get(metin)
        if yeni is None:
            yeni = _betik_duzelt(metin, ceviri, kodlama if sabit else None)
            if yeni == metin:
                out += blob[p:p + 4 + n]
                p += 4 + n
                continue
        if sabit:
            dolu = _doldur(yeni, n, kodlama)
            if dolu is None:
                if sigmayan is not None:
                    sigmayan.append((metin, yeni, len(yeni.encode(kodlama)) - n))
                out += blob[p:p + 4 + n]
                p += 4 + n
                continue
            yeni = dolu
        ham = yeni.encode(kodlama)
        out += struct.pack('<I', len(ham)) + ham
        degisen += 1
        p += 4 + n
    struct.pack_into('<I', out, 0, len(out))       # blob kendi uzunlugunu tasir
    return bytes(out), degisen


def yaz(ham, ceviri, kodlama='cp1254', sabit=True, sigmayan=None):
    """ham: charroles.rdb baytlari -> (yeni_baytlar, degisen, kayit_sayisi)"""
    idx = struct.unpack('<I', ham[4:8])[0]
    base = 8 + idx
    degisen = 0
    if sabit:
        # YERINDE YAZIM: her blob orijinal uzunlugunu korudugu icin dosya
        # duzenine hic dokunmuyoruz - indeks, blob sirasi ve aradaki her bayt
        # oldugu gibi kaliyor. (Bloklar dosyada sirali degil; yeniden paketlemek
        # onlari tasirdi.)
        out = bytearray(ham)
        for i in range(8, 8 + idx, 16):
            a, f, o, l = struct.unpack('<4I', ham[i:i + 16])
            if o + l > len(ham) - base or l < 4:
                continue
            blob = ham[base + o:base + o + l]
            nb, d = blob_yaz(blob, ceviri, kodlama, True, sigmayan)
            assert len(nb) == len(blob), 'sabit modda uzunluk degisti'
            out[base + o:base + o + l] = nb
            degisen += d
        return bytes(out), degisen, idx // 16

    yeni_idx, govde = bytearray(), bytearray()
    for i in range(8, 8 + idx, 16):
        a, f, o, l = struct.unpack('<4I', ham[i:i + 16])
        if o + l > len(ham) - base or l < 4:
            yeni_idx += ham[i:i + 16]              # bozuk/dolgu girisi: aynen
            continue
        blob = ham[base + o:base + o + l]
        nb, d = blob_yaz(blob, ceviri, kodlama, False, sigmayan)
        degisen += d
        yeni_idx += struct.pack('<4I', a, f, len(govde), len(nb))
        govde += nb
    assert len(yeni_idx) == idx, 'indeks boyutu degisti'
    return ham[:4] + struct.pack('<I', idx) + bytes(yeni_idx) + bytes(govde), degisen, idx // 16


def duz_yaz(ham, ceviri, boyut_alani=4, kodlama='cp1254', sabit=True, sigmayan=None):
    """Tek parca, indekssiz dosyalar icin (narrator.rcd).

    narrator.rcd dosya uzunlugunu 0x04'te tutar; blob_yaz 0x00'i guncelledigi
    icin burada dogru alani ayrica yaziyoruz.
    """
    out, degisen = blob_yaz(ham, ceviri, kodlama, sabit, sigmayan)
    out = bytearray(out)
    out[0:4] = ham[0:4]                              # blob_yaz'in dokundugu alani geri al
    struct.pack_into('<I', out, boyut_alani, len(out))
    return bytes(out), degisen


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    d = open('ext2/charroles.rdb', 'rb').read()
    aynen, deg, n = yaz(d, {}, 'latin-1')
    print('kimlik testi (%d kayit): %s' % (n, 'GECTI' if aynen == d else 'KALDI'))
    import charroles_tr
    yeni, deg, n = yaz(d, charroles_tr.TR)
    print('ceviri: %d dizi degisti, %d -> %d bayt' % (deg, len(d), len(yeni)))
