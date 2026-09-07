# -*- coding: utf-8 -*-
"""RDB (Bare Mettle kayit veritabani) okuma / yeniden yazma.

BICIM
  0x00  u32 magic          (objstrings.rdb icin 02 0c bf af)
  0x04  u32 index_size     (bayt)
  0x08  index              16 baytlik kayitlar: [a:u32][f:u32][offset:u32][length:u32]
  8+index_size  veri havuzu  (offset bu noktaya goredir, metinler null ile bitmez)

Metinler havuzda paylasilabilir; yeniden yazarken ayni metni bir kez koyup
tum kayitlari ayni offsete yonlendiririz (orijinalde de boyle).
"""
import struct

MAGIC_STR = 0xAFBF0C02


def oku(b):
    """-> (magic, [ (a, f, metin) ], ham_index)"""
    magic, idx = struct.unpack('<II', b[:8])
    base = 8 + idx
    kayit = []
    for i in range(8, 8 + idx, 16):
        a, f, o, l = struct.unpack('<4I', b[i:i + 16])
        if o + l > len(b) - base:
            kayit.append((a, f, None))          # bozuk/dolgu girisi: aynen korunur
        else:
            kayit.append((a, f, b[base + o:base + o + l].decode('latin-1')))
    return magic, kayit


def yaz(b, ceviri, kodlama='cp1254'):
    """ceviri: {ingilizce: turkce}. Eslesmeyen metinler aynen kalir."""
    magic, kayit = oku(b)
    idx = struct.unpack('<I', b[4:8])[0]
    havuz = bytearray()
    yer = {}
    yeni_idx = bytearray()
    for j, (a, f, metin) in enumerate(kayit):
        if metin is None:                        # dokunma
            yeni_idx += b[8 + j * 16:8 + j * 16 + 16]
            continue
        yeni = ceviri.get(metin, metin)
        try:
            ham = yeni.encode(kodlama)
        except UnicodeEncodeError:
            ham = metin.encode('latin-1')
        if ham not in yer:
            yer[ham] = len(havuz)
            havuz += ham
        yeni_idx += struct.pack('<4I', a, f, yer[ham], len(ham))
    assert len(yeni_idx) == idx, 'index boyutu degisti'
    return b[:4] + struct.pack('<I', idx) + bytes(yeni_idx) + bytes(havuz)


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    d = open('ext2/objstrings.rdb', 'rb').read()
    aynen = yaz(d, {})
    m1, k1 = oku(d)
    m2, k2 = oku(aynen)
    print('kimlik testi: kayitlar ayni mi ->', k1 == k2)
    print('boyut %d -> %d (tekrar eden metinler tekillestirildi)' % (len(d), len(aynen)))
