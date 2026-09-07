# -*- coding: utf-8 -*-
"""EXANIMA TURKCE YAMA - kurulum programi.

Bu program yamayi TASIMAZ, URETIR: oyunun kendi dosyalarindan okuyup Turkce
surumu yerinde olusturur. Bu yuzden paket birkac yuz kilobayt kalir ve oyun
guncellendiginde yeniden calistirmak yeterlidir.

CALISMA MANTIGI
  1) Oyun klasoru bulunur (Steam kutugu -> kutuphane listesi -> elle giris).
  2) Exanima.exe ve Resource.rpk'nin ORIJINAL yedegi alinir (.orijinal).
     Yedek zaten varsa ve oyun guncellenmisse yedek tazelenir.
  3) Yama yedeklerden uretilip oyun dosyalarinin uzerine yazilir.
  Kaldirma islemi yedekleri geri kopyalar.

GUVENLIK
  Yedek yoksa ve mevcut dosya ZATEN YAMALIYSA islem durdurulur - yoksa yamali
  dosya "orijinal" diye kaydedilir ve geri donus imkani kaybolur.

EKRANA BASILAN METINLER
  Turkce harfli. Python, Windows konsoluna WriteConsoleW ile yazdigi icin
  kod sayfasindan bagimsiz olarak dogru gorunur; ayrica chcp 65001 cagrilir.
"""
import os
import shutil
import sys

SURUM = '1.0'
ORIJ = '.orijinal'
DOSYALAR = ('Exanima.exe', 'Resource.rpk')

# Yamanin kendi imzasi: bu diziler yalnizca yamali dosyalarda bulunur.
IMZA = {
    'Exanima.exe': ('Yer De\u011fi\u015ftirme'.encode('cp1254'),
                    'B\u0130R TU\u015eA BASIN'.encode('cp1254')),
    'Resource.rpk': ('Kafes Demiri'.encode('cp1254'),
                     'Me\u015fale'.encode('cp1254')),
}


def yaz(*a):
    print(*a)
    sys.stdout.flush()


def baslik():
    yaz('=' * 58)
    yaz('   E X A N I M A   -   T Ü R K Ç E   Y A M A   v%s' % SURUM)
    yaz('=' * 58)
    yaz()


# ------------------------------------------------------------ oyun klasoru
def steam_kutuphaneleri():
    """Steam kutugundan ve kutuphane listesinden olasi kok dizinler."""
    kokler = []
    try:
        import winreg
        for kok, yol in ((winreg.HKEY_CURRENT_USER, r'Software\Valve\Steam'),
                         (winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\WOW6432Node\Valve\Steam')):
            try:
                with winreg.OpenKey(kok, yol) as k:
                    for ad in ('SteamPath', 'InstallPath'):
                        try:
                            kokler.append(winreg.QueryValueEx(k, ad)[0])
                        except OSError:
                            pass
            except OSError:
                pass
    except ImportError:
        pass

    kutuphane = list(kokler)
    for k in kokler:
        vdf = os.path.join(k, 'steamapps', 'libraryfolders.vdf')
        try:
            with open(vdf, encoding='utf-8', errors='replace') as f:
                metin = f.read()
        except OSError:
            continue
        # satirlar:  "path"   "D:\\SteamLibrary"
        for parca in metin.split('"path"')[1:]:
            try:
                kutuphane.append(parca.split('"')[1].replace('\\\\', '\\'))
            except IndexError:
                pass
    return kutuphane


def oyunu_bul():
    adaylar = []
    for k in steam_kutuphaneleri():
        adaylar.append(os.path.join(k, 'steamapps', 'common', 'Exanima'))
    for surucu in 'CDEFGHIJ':
        for kalip in (r'{0}:\Steam\steamapps\common\Exanima',
                      r'{0}:\SteamLibrary\steamapps\common\Exanima',
                      r'{0}:\Program Files (x86)\Steam\steamapps\common\Exanima',
                      r'{0}:\Games\Exanima',
                      r'{0}:\Exanima'):
            adaylar.append(kalip.format(surucu))
    gorulen = set()
    for a in adaylar:
        n = os.path.normpath(a)
        if n.lower() in gorulen:
            continue
        gorulen.add(n.lower())
        if os.path.isfile(os.path.join(n, 'Exanima.exe')):
            return n
    return None


def yolu_sor():
    """Otomatik bulma basarisiz oldugunda klasoru kullaniciya adim adim sordurur.

    Buraya dusen kisi bilgisayarla arasi iyi olmayabilir; "yolu kopyala" gibi
    kestirme tarifler yerine Steam uzerinden tikla-kopyala anlatiliyor.
    """
    yaz('Oyunun kurulu olduğu klasör otomatik bulunamadı.')
    yaz('Klasörü elle göstermeniz gerekiyor. Şöyle bulabilirsiniz:')
    yaz()
    yaz('   1.  Steam\'i açın.')
    yaz('   2.  Kitaplık\'ta Exanima\'nın üzerine SAĞ TIKLAYIN.')
    yaz('   3.  Açılan menüden:  Yönet  >  Yerel dosyalara gözat')
    yaz('       Karşınıza çıkan pencere oyunun klasörüdür.')
    yaz('   4.  O pencerenin EN ÜSTÜNDEKİ adres çubuğuna bir kez tıklayın.')
    yaz('       Oradaki yazı mavi renkte seçili hâle gelecek.')
    yaz('   5.  Ctrl+C ile kopyalayın.')
    yaz('   6.  Bu pencereye dönüp Ctrl+V ile yapıştırın, Enter\'a basın.')
    yaz('       (Ctrl+V çalışmazsa buraya sağ tıklayın, yapıştırır.)')
    yaz()
    yaz('   Kopyaladığınız yazı şuna benzer bir şey olacak:')
    yaz('      E:\\Steam\\steamapps\\common\\Exanima')
    yaz()
    yaz('   Vazgeçmek için hiçbir şey yazmadan Enter\'a basın.')
    yaz()
    while True:
        y = input('Klasör: ').strip().strip('"').strip()
        if not y:
            return None
        y = os.path.normpath(y)
        if os.path.isfile(os.path.join(y, 'Exanima.exe')):
            return y
        yaz()
        yaz('   Bu klasörün içinde Exanima.exe yok:')
        yaz('      %s' % y)
        yaz('   Yanlış klasörü kopyalamış olabilirsiniz. Yukarıdaki')
        yaz('   adımları tekrar deneyin, ya da Enter\'a basıp çıkın.')
        yaz()


# ------------------------------------------------------------ yedekler
def yamali_mi(yol, ad):
    """Dosya BIZIM yamamizi tasiyor mu?"""
    try:
        with open(yol, 'rb') as f:
            ham = f.read()
    except OSError:
        return False
    return any(im in ham for im in IMZA[ad])


def yazilabilir_mi(yol):
    try:
        with open(yol, 'r+b'):
            return True
    except OSError:
        return False


def yedekleri_hazirla(oyun):
    """-> (tamam_mi, mesaj). Gerekirse yedek olusturur veya tazeler."""
    for ad in DOSYALAR:
        canli = os.path.join(oyun, ad)
        yedek = canli + ORIJ
        if not os.path.exists(canli):
            return False, 'Oyun dosyası eksik: %s' % ad
        if not os.path.exists(yedek):
            if yamali_mi(canli, ad):
                return False, (
                    '%s zaten yamalı ama orijinal yedeği yok.\n'
                    '  Steam > Exanima > Özellikler > Yüklü Dosyalar >\n'
                    '  "Oyun dosyalarının bütünlüğünü doğrula" çalıştırın,\n'
                    '  sonra bu programı tekrar açın.' % ad)
            yaz('  yedek alınıyor : %s%s' % (ad, ORIJ))
            shutil.copy2(canli, yedek)
        elif not yamali_mi(canli, ad) and os.path.getsize(canli) != os.path.getsize(yedek):
            # Oyun guncellenmis: Steam canli dosyayi yenilemis, yedek eskimis.
            yaz('  oyun güncellenmiş, yedek tazeleniyor: %s' % ad)
            shutil.copy2(canli, yedek)
        else:
            yaz('  yedek hazır    : %s%s' % (ad, ORIJ))
    return True, ''


# ------------------------------------------------------------ islemler
def kur(oyun):
    for ad in DOSYALAR:
        if not yazilabilir_mi(os.path.join(oyun, ad)):
            yaz('HATA: %s dosyasına yazılamıyor.' % ad)
            yaz('  Oyun büyük ihtimalle açık. Exanima\'yı tamamen kapatıp')
            yaz('  tekrar deneyin.')
            return 1
    yaz('[1] Yedekler')
    tamam, mesaj = yedekleri_hazirla(oyun)
    if not tamam:
        yaz('HATA: %s' % mesaj)
        return 1
    yaz()
    import uygula
    sonuc = uygula.main(oyun)
    if sonuc:
        return sonuc
    yaz()
    yaz('KURULUM TAMAMLANDI. İyi oyunlar!')
    return 0


def kaldir(oyun):
    eksik = [a for a in DOSYALAR if not os.path.exists(os.path.join(oyun, a + ORIJ))]
    if eksik:
        yaz('HATA: yedek bulunamadı: %s' % ', '.join(eksik))
        yaz('  Steam üzerinden "Oyun dosyalarının bütünlüğünü doğrula"')
        yaz('  seçeneğini kullanın.')
        return 1
    for ad in DOSYALAR:
        if not yazilabilir_mi(os.path.join(oyun, ad)):
            yaz('HATA: %s dosyasına yazılamıyor. Oyun açık olabilir.' % ad)
            return 1
    for ad in DOSYALAR:
        yaz('  geri yükleniyor: %s' % ad)
        shutil.copy2(os.path.join(oyun, ad + ORIJ), os.path.join(oyun, ad))
    yaz()
    yaz('YAMA KALDIRILDI. Oyun İngilizce hâline döndü.')
    return 0


def main():
    if os.name == 'nt':
        os.system('chcp 65001 >nul 2>&1')
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

    baslik()
    arg = sys.argv[1:]
    oyun = None
    if '--yol' in arg:
        i = arg.index('--yol')
        if i + 1 < len(arg):
            oyun = arg[i + 1]
    oyun = oyun or oyunu_bul() or yolu_sor()
    if not oyun:
        yaz('Oyun bulunamadı, çıkılıyor.')
        return 1

    if '--kur' in arg:
        return kur(oyun)
    if '--kaldir' in arg:
        return kaldir(oyun)

    while True:
        yaz()
        yaz('  Oyun: %s' % oyun)
        yaz()
        yaz('  1) Türkçe yamayı KUR')
        yaz('  2) Yamayı KALDIR (oyunu İngilizceye döndür)')
        yaz('  3) Çıkış')
        yaz()
        try:
            s = input('  Seçiminiz [1/2/3]: ').strip()
        except (EOFError, KeyboardInterrupt):
            return 0
        yaz()
        if s == '1':
            kur(oyun)
        elif s == '2':
            kaldir(oyun)
        elif s == '3':
            return 0
        else:
            continue
        yaz()
        try:
            input('Kapatmak için Enter\'a basın...')
        except (EOFError, KeyboardInterrupt):
            pass
        return 0


if __name__ == '__main__':
    sys.exit(main())
