# -*- coding: utf-8 -*-
"""Sigmayan diyalog satirlarini baglamiyla birlikte JSON'a cikarir."""
import struct, sys, json, io
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import tr_charroles as TC, charroles_tr

ham = open('ext2/charroles.rdb', 'rb').read()
idx = struct.unpack('<I', ham[4:8])[0]
base = 8 + idx

# her dizinin hangi rolde, hangi komsularla gectigini bul
yer = {}
for i in range(8, 8 + idx, 16):
    a, f, o, l = struct.unpack('<4I', ham[i:i + 16])
    if o + l > len(ham) - base or l < 4:
        continue
    b = ham[base + o:base + o + l]
    rol = b[8:24].split(b'\x00')[0].decode('latin-1')
    ss, p = [], 0
    while p < len(b):
        d = TC._dizi(b, p)
        if d is None:
            p += 1
            continue
        ss.append(d[1])
        p += 4 + d[0]
    for j, s in enumerate(ss):
        if s not in yer:
            yer[s] = (rol, ss[j - 1] if j else '', ss[j + 1] if j + 1 < len(ss) else '')

sig = []
TC.yaz(ham, charroles_tr.TR, sigmayan=sig)
benzersiz = {}
for en, tr, tasma in sig:
    benzersiz[en] = (tr, tasma)

cikti = []
for en, (tr, tasma) in benzersiz.items():
    rol, onc, son = yer.get(en, ('?', '', ''))
    cikti.append({
        'rol': rol,
        'butce': len(en.encode('latin-1')),
        'tasma': tasma,
        'en': en,
        'tr': tr,
        'onceki': onc[:110],
        'sonraki': son[:110],
    })
cikti.sort(key=lambda x: (-x['tasma'], x['rol']))
json.dump(cikti, io.open('sigmayan.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('sigmayan benzersiz satir:', len(cikti))
print('roller:', sorted({x['rol'] for x in cikti}))
print('tasma toplami: %d bayt, ortalama %.1f, en buyuk %d'
      % (sum(x['tasma'] for x in cikti), sum(x['tasma'] for x in cikti) / len(cikti),
         max(x['tasma'] for x in cikti)))
