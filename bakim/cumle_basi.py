# -*- coding: utf-8 -*-
"""Esya aciklamalarinda cumle basi buyuk harf duzeltmesi (tek seferlik).

    python cumle_basi.py          -> yalnizca raporlar
    python cumle_basi.py --yaz    -> obj_tr.json'u gunceller

NEDEN
  Ingilizce aciklamalar iki turlu: bazilari tam cumle ('A simple torch.'),
  bazilari onune bir kalite/malzeme sifati gelen parca ('leather cap.').
  Once itemin adi cumle ortasinda buyuk yazilmasin diye topluca kucultmustum;
  bu, TAM CUMLE olanlarin da bas harfini kucultmus ve oyunda
  "basit bir meşale." gibi gorunuyordu.

KURAL
  Ingilizcesi buyuk harfle basliyorsa Turkcesi de buyuk harfle baslar.
  Ingilizcesi kucukse (parca) dokunulmaz. Cumle ICINDEKI kelimeler
  degistirilmez - bu yalnizca ilk harfi ilgilendirir.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
YOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'obj_tr.json')


def ilk_harf(s):
    for i, c in enumerate(s):
        if c.isalpha():
            return i, c
    return -1, ''


def tr_buyut(c):
    return 'İ' if c == 'i' else c.upper()


def main(yaz=False):
    veri = json.load(io.open(YOL, encoding='utf-8'))
    degisen = []
    for x in veri:
        if x['kind'] != 'aciklama':
            continue
        _, en_c = ilk_harf(x['en'])
        i, tr_c = ilk_harf(x['tr'])
        if not en_c.isupper() or i < 0 or not tr_c.islower():
            continue
        eski = x['tr']
        x['tr'] = eski[:i] + tr_buyut(tr_c) + eski[i + 1:]
        degisen.append((eski, x['tr']))
    print('%d aciklamanin bas harfi buyutuldu' % len(degisen))
    for a, b in degisen[:8]:
        print('  %-46r -> %r' % (a[:44], b[:46]))
    if yaz:
        with io.open(YOL, 'w', encoding='utf-8') as f:
            json.dump(veri, f, ensure_ascii=False, indent=1)
        print('obj_tr.json yazildi')
    else:
        print('(deneme - yazmak icin --yaz)')


if __name__ == '__main__':
    main('--yaz' in sys.argv)
