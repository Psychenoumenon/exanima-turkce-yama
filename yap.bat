@echo off
rem ===================================================================
rem  Exanima Turkce Yama - tek dosyalik yukleyiciyi derler
rem
rem  Gereksinim:  Python 3.10+  ve  pip install pyinstaller
rem  Cikti     :  dist\ExanimaTurkceYama.exe   (~8.5 MB)
rem
rem  numpy'a gerek YOKTUR; --exclude-module ile disarida birakilir,
rem  yoksa ortamda kurulu oldugunda pakete girip boyutu kat kat
rem  buyutur.
rem ===================================================================

python -m PyInstaller --onefile --console --clean --noconfirm ^
  --name ExanimaTurkceYama ^
  --version-file surum_bilgisi.txt ^
  --add-data "tr_anchors.json;." ^
  --add-data "obj_tr.json;." ^
  --add-data "exefonts_TR_hash.pkl;." ^
  --add-data "fontbase24r_TR2.rfi;." ^
  --hidden-import uygula ^
  --exclude-module numpy ^
  --exclude-module PIL ^
  --exclude-module tkinter ^
  --exclude-module matplotlib ^
  --exclude-module scipy ^
  --exclude-module pytest ^
  kur.py

echo.
echo Bitti. Cikti: dist\ExanimaTurkceYama.exe
pause
