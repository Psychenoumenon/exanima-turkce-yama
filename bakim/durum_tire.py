# -*- coding: utf-8 -*-
"""Esya durum ifadelerini "- Baslik Duzeni" bicimine cevirir (tek seferlik).

    python durum_tire.py          -> yalnizca raporlar
    python durum_tire.py --yaz    -> tr_anchors.json'u gunceller

NEDEN TIRE, VIRGUL DEGIL
  Oyun durumu "<aciklama> + BOSLUK + <durum> + ." seklinde birlestiriyor.
  O bosluk exe'de tek bir Delphi sabiti ve 8 ayri cagri yerinden kullaniliyor;
  virgule cevirmek kalite sifati ile esya adi arasini da bozardi. Tireyi durum
  metninin BASINA koyunca ayni gorsel ayrimi risksiz elde ediyoruz:
      "İyi el testeresi" + " " + "- İyi Durumda" + "."
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
YOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tr_anchors.json')
DURUM = re.compile(r'^in .+ condition$')


def tr_buyut(c):
    return 'İ' if c == 'i' else c.upper()


def tr_baslik(s):
    return ' '.join(tr_buyut(w[0]) + w[1:] if w else w for w in s.split(' '))


def main(yaz=False):
    veri = json.load(io.open(YOL, encoding='utf-8'))
    gorulen, n = {}, 0
    for a in veri:
        if not DURUM.match(a['en']) or a['tr'].startswith('- '):
            continue
        a['tr'] = '- ' + tr_baslik(a['tr'])
        gorulen[a['en']] = a['tr']
        n += 1
    print('%d capa guncellendi (%d benzersiz durum)' % (n, len(gorulen)))
    for en, tr in sorted(gorulen.items()):
        print('  %-30s -> %r' % (en, tr))
    if yaz:
        with io.open(YOL, 'w', encoding='utf-8') as f:
            json.dump(veri, f, ensure_ascii=False, indent=1)
        print('\ntr_anchors.json yazildi')
    else:
        print('\n(deneme - yazmak icin --yaz)')


if __name__ == '__main__':
    main('--yaz' in sys.argv)
