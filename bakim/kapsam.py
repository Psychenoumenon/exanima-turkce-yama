# -*- coding: utf-8 -*-
"""KAPSAMA RAPORU: yamali Resource.rpk'daki her metin kabini yapisal olarak okur
ve hala Ingilizce duran metinleri listeler. Ham bayt taramasindan farkli olarak
KISA etiketleri de yakalar."""
import io, json, re, struct, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import uygula, tr_rdb, tr_pwr, tr_rfc, tr_charroles as TC
import charroles_tr, rfc_tr, pwr_tr, manual_tr

G = r'E:\Steam\steamapps\common\Exanima'
raw, i0, kayit = uygula.rpk_oku(G + r'\Resource.rpk'); base = 8+i0
ic = {ad: raw[base+o:base+o+s] for ad,o,s,_ in kayit}

TRC = set(charroles_tr.TR) | set(charroles_tr.NARRATOR) | set(rfc_tr.TR) | set(pwr_tr.TR)
TRC |= {d['en'] for d in json.load(io.open('obj_tr.json', encoding='utf-8'))}
TURKCE = re.compile(r'[çğıöşüÇĞİÖŞÜâîû]')
INGILIZCE = re.compile(r'\b(the|and|of|to|you|your|is|are|with|for|that|this|it|'
                       r'a|an|in|on|be|not|can|will|has|have|from|or|but|they)\b', re.I)

def ing_mi(s):
    if not s:
        return False
    t = s.strip()
    if len(t) < 3 or TURKCE.search(t):
        return False
    if t in TRC:                       # cevirisi var ama uygulanmamis
        return True
    if not re.search(r'[A-Za-z]{3}', t):
        return False
    return bool(INGILIZCE.search(t)) or t in TRC

def diziler_charroles(b):
    idx = struct.unpack('<I', b[4:8])[0]; bb = 8+idx
    for i in range(8, 8+idx, 16):
        a,f,o,l = struct.unpack('<4I', b[i:i+16])
        if o+l > len(b)-bb or l<4: continue
        blob = b[bb+o:bb+o+l]; p=0
        while p < len(blob):
            d = TC._dizi(blob,p)
            if d is None: p+=1; continue
            yield d[1]; p += 4+d[0]

rapor = {}
_, kay = tr_rdb.oku(ic['objstrings.rdb'])
rapor['objstrings.rdb'] = [t for _,_,t in kay if ing_mi(t)]
for ad in sorted(a for a in ic if a.endswith('.pwr')):
    _, kk = tr_pwr.coz(ic[ad])
    rapor[ad] = [t for _o, t in kk if ing_mi(t)]
rapor['charroles.rdb'] = [t for t in diziler_charroles(ic['charroles.rdb'])
                          if ing_mi(t) and not TC._betik_mi(t)]
p = 0; nar = []
nb = ic['narrator.rcd']
while p < len(nb):
    d = TC._dizi(nb, p)
    if d is None: p += 1; continue
    nar.append(d[1]); p += 4 + d[0]
rapor['narrator.rcd'] = [t for t in nar if ing_mi(t) and not TC._betik_mi(t)]
for ad in sorted(a for a in ic if a.endswith('.rfc')):
    kk = []
    for pp, idx, hav in tr_rfc.gomulu_rdb(ic[ad]):
        _, k2 = tr_rdb.oku(ic[ad][pp:pp+8+idx+hav])
        kk += [t for _,_,t in k2]
    v = [t for t in kk if ing_mi(t)]
    if v: rapor[ad] = v
for ad in ('manualkm.fds','manualcn.fds'):
    b = ic[ad]; n2 = struct.unpack('<I', b[4:8])[0]; bb = 8+n2
    v = []
    for j in range(8, 8+n2, 32):
        o2, s2 = struct.unpack('<II', b[j+16:j+24])
        t = b[bb+o2:bb+o2+s2].decode('cp1254','replace')
        if ing_mi(t): v.append(t[:80])
    rapor[ad] = v

top = 0
for ad, v in sorted(rapor.items()):
    if v:
        print('=== %s : %d' % (ad, len(v)))
        for t in v[:12]: print('    %r' % t[:110])
        top += len(v)
print()
print('TOPLAM kalan Ingilizce metin:', top)
print()
print('--- THIS IS A DUPE nerede ---')
for ad, o, s, _ in kayit:
    if b'THIS IS A DUPE' in raw[base+o:base+o+s]:
        b = raw[base+o:base+o+s]; k = b.find(b'THIS IS A DUPE')
        print('   %s @%d  baglam=%r' % (ad, k, b[k-60:k+40].decode('latin-1')))
