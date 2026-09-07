# -*- coding: utf-8 -*-
"""TAM DENETIM: oyundaki her dosyada oyuncuya gorunebilecek Ingilizce metin ara.

Yontem
  Dosyalari akis halinde okur, yazdirilabilir ASCII kosularini cikarir ve
  Ingilizce NESIR gibi gorunenleri isaretler. Ic tanimlayicilar (mesh/material
  adlari, dosya yollari, shader kaynagi, ayar anahtarlari) elenir.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

OYUN = r'E:\Steam\steamapps\common\Exanima'
KOSU = re.compile(rb'[\x20-\x7e\r\n\t]{14,600}')
KELIME = re.compile(r"[A-Za-z']+")

ING = {'the','and','of','to','in','is','it','you','that','for','with','this',
       'are','be','on','as','your','from','or','an','can','will','not','has',
       'have','at','by','but','they','their','was','were','all','one','more',
       'when','if','there','some','其'}
# eleme: teknik / gelistirici icerigi
ELE = re.compile(
    r'void main|uniform |gl_[A-Za-z]|vec[234] |sampler2D|#version|layout\(|'
    r'in vec|out vec|\.rpk|\.rfi|\.rfc|\.rdb|\.dll|\.exe|C:\\|/usr/|'
    r'Copyright|OpenAL|OpenGL|Direct3D|libcurl|zlib|Steam|Delphi|FastMM|'
    r'[A-Za-z0-9_]{24,}|^\s*[A-Za-z_][A-Za-z0-9_]*\s*=\s*[-0-9.]+\s*;?\s*$')


def ingilizce_mi(s):
    if ELE.search(s):
        return False
    k = [w.lower() for w in KELIME.findall(s)]
    if len(k) < 4:
        return False
    ortak = sum(1 for w in k if w in ING)
    if ortak < 2:
        return False
    # harf yogunlugu: tanimlayici salkimlarini ele
    harf = sum(c.isalpha() or c in " ,.'!?-" for c in s)
    return harf / len(s) > 0.90


def tara(yol, etiket=None):
    ad = etiket or os.path.basename(yol)
    boy = os.path.getsize(yol)
    bulgu, gorulen = [], set()
    ARTIK = 600
    with open(yol, 'rb') as f:
        artik = b''
        okundu = 0
        while True:
            blok = f.read(1 << 24)
            if not blok:
                break
            okundu += len(blok)
            veri = artik + blok
            for m in KOSU.finditer(veri):
                s = m.group().decode('latin-1').strip()
                if len(s) < 14 or s in gorulen:
                    continue
                if ingilizce_mi(s):
                    gorulen.add(s)
                    bulgu.append(s)
            artik = veri[-ARTIK:]
    return ad, boy, bulgu


if __name__ == '__main__':
    hedef = sys.argv[1:] or sorted(
        os.path.join(OYUN, f) for f in os.listdir(OYUN)
        if f.endswith(('.rpk', '.exe', '.rfp', '.ini')) and '.orijinal' not in f)
    rapor = {}
    for yol in hedef:
        ad, boy, bulgu = tara(yol)
        rapor[ad] = bulgu
        print('%-20s %10.1f MB  ->  %d aday' % (ad, boy / 1e6, len(bulgu)))
        sys.stdout.flush()
    json.dump(rapor, io.open('denetim.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('\ndenetim.json yazildi, toplam %d aday'
          % sum(len(v) for v in rapor.values()))
