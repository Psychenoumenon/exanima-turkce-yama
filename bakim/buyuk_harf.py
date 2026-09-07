# -*- coding: utf-8 -*-
"""Esya adi / aciklama buyuk-kucuk harf duzeltmesi.

OYUNUN CUMLE KURGUSU (exe 0x32DD48 civarindaki parca sabitlerinden cozuldu):

    <kalite sifati> + " " + <esya aciklamasi> + " " + <durum ifadesi> + "."
    ornek: "oldukca iyi yapilmis" + "bir cift hafif kumas pantolon" + "biraz
            yipranmis durumda" + "."

Yani esya aciklamasi CUMLENIN ORTASINDA duruyor. Ingilizce veride bunun icin
her esyanin IKI bicimi var:
    'Bardiche'  -> baslikta gorunen ad          (Basligin Her Kelimesi Buyuk)
    'bardiche'  -> cumle icinde gecen bicim     (tamami kucuk)
Ilk cevirinin ikisini de buyuk harfle yazmasi, "ilkel El Baltasi iyi durumda."
gibi cumle ortasinda buyuk harf birakiyordu.

KURAL
  1. Ingilizcesi kucuk harfle ya da '-' ile basliyorsa -> Turkcesi TAMAMEN kucuk.
  2. Ingilizcesi 'A '/'An ' ile baslayan kalip aciklamalarda -> yalnizca ilk
     harf kucultulur (geri kalani zaten cumle duzeninde).
  3. Baslik adlari (Ingilizcesi buyuk harfle baslayan kisa adlar) degismez.
  4. Anlati metinleri (@WEAR, 'This ...', 'When you ...', coklu cumle) degismez.

Turkce'ye ozgu kucultme: I -> 'ı', İ -> 'i' (Python'un lower()'i I'yi 'i' yapar,
bu Turkce'de yanlistir).

Kullanim: python buyuk_harf.py          -> yalnizca degisiklikleri listeler
          python buyuk_harf.py --yaz    -> obj_tr.json'a yazar
"""
import re

# Anlati metni: buyuk harfle basladigi gibi kalmali
ANLATI = re.compile(r'^@WEAR|^(This|That|These|Those|When|You|Your|It |They |As )\b')

# Kalip esya aciklamasi: "A ..." / "An ..." ile baslayan tek cumlelik isim obegi
KALIP = re.compile(r'^(A|An) [^.!?]*\.?$')


def tr_kucult(s):
    """Turkce dogru kucultme (I->ı, İ->i)."""
    return s.replace('I', 'ı').replace('İ', 'i').lower()


def ilk_harf_kucult(s):
    for i, ch in enumerate(s):
        if ch.isalpha():
            return s[:i] + tr_kucult(ch) + s[i + 1:]
    return s


def duzelt(kayit):
    """kayit: {'en','tr','kind'} -> (yeni_tr, sebep) ; degismediyse sebep None."""
    en, tr, kind = kayit['en'], kayit['tr'], kayit['kind']

    # 1. cumle ici ad bicimleri
    if kind == 'ad':
        cekirdek = en[1:] if en.startswith('-') else en
        if cekirdek[:1].islower():
            yeni = ('-' if tr.startswith('-') else '') + tr_kucult(tr.lstrip('-'))
            return (yeni, 'cumle-ici ad') if yeni != tr else (tr, None)
        return tr, None

    # 2. kalip aciklamalar
    if kind == 'aciklama' and not ANLATI.match(en) and KALIP.match(en.replace('\x10', 'x')):
        yeni = ilk_harf_kucult(tr)
        return (yeni, 'kalip aciklama') if yeni != tr else (tr, None)

    return tr, None


if __name__ == '__main__':
    import io
    import json
    import sys
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    yol = 'obj_tr.json'
    veri = json.load(io.open(yol, encoding='utf-8'))
    n = {}
    for k in veri:
        yeni, sebep = duzelt(k)
        if sebep:
            n[sebep] = n.get(sebep, 0) + 1
            print('  [%-14s] %-40s %r -> %r' % (sebep, k['en'][:40], k['tr'][:44], yeni[:44]))
            k['tr'] = yeni
    if '--yaz' in sys.argv:
        json.dump(veri, io.open(yol, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('\nobj_tr.json guncellendi.')
    print('\nOZET:', n)
