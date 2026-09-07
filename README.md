# Exanima Turkish Translation Patch

Complete Turkish translation for [Exanima](https://store.steampowered.com/app/362490/Exanima/)
by Bare Mettle Entertainment. Unofficial, fan-made, free.

This repository contains the **full source** of the patch and its installer.

---

## What it does

The installer does **not** ship patched game files. It reads the player's own
game files, generates the Turkish version in place, and writes it back. That is
why the download is small and why re-running it after a game update is enough.

Translated: user interface, settings, 683 item names and descriptions, the four
power trees, the in-game manual, 725 NPC dialogue lines, 126 in-world books and
notes, narrator text, and character backgrounds.

Turkish characters (c g i I o s u with diacritics) are rendered by drawing the
missing glyphs into the game's own font atlases and correcting the advance-width
tables accordingly.

## How to build

Requirements: Python 3.10+ on Windows.

```
pip install pyinstaller
yap.bat
```

Output: `dist/ExanimaTurkceYama.exe` (~8.5 MB).

`yap.bat` is a single PyInstaller invocation. `--exclude-module numpy` matters:
if numpy is present in the environment it gets bundled and multiplies the size.

To run without building:

```
python kur.py
```

## Note on antivirus false positives

The released binary is packaged with PyInstaller in `--onefile` mode. Some
scanners flag PyInstaller one-file executables generically (for example
`Trojan:Script/Wacatac.C!ml`), because the bootstrap unpacks itself to a
temporary directory before running. This is a heuristic verdict about the
packaging format, not about the code.

The program makes no network connections, installs no services, and creates no
persistence. It reads the Steam registry key to locate the game, copies the two
original files to `.orijinal` backups, and rewrites them. Everything it does is
in this repository, and the released executable can be reproduced from it with
the command above.

## File map

| File | Purpose |
|---|---|
| `kur.py` | Installer entry point: find game, back up, install, uninstall |
| `uygula.py` | Applies every translation stage to the game files |
| `tr_patch2.py` | Context-anchored string patching of `Exanima.exe` |
| `tr_anchors.json` | 935 translation anchors, each keyed by its neighbouring strings |
| `obj_tr.json` | 683 item names and descriptions |
| `charroles_tr.py` | NPC dialogue and narrator lines |
| `manual_tr.py` | In-game manual |
| `pwr_tr.py` / `tr_pwr.py` | Power trees |
| `rfc_tr.py` / `tr_rfc.py` | UI layout resources |
| `tr_rdb.py` | RDB archive reader/writer |
| `tr_charroles.py` | Fixed-length in-place writer for the dialogue database |
| `rfi_codec.py` | Rayform Image codec (font atlases) |
| `tr_widths.py` | Font advance-width table patching |
| `fontbase24r_TR2.rfi`, `exefonts_TR_hash.pkl` | Font atlases with Turkish glyphs |
| `bakim/` | Maintenance scripts used while producing the translation |

## How the exe patching survives game updates

Strings are not located by fixed offsets. Each one is identified by its
neighbouring strings in the binary, resolved in the order
`(text, previous, next)` then `(text, previous)` then `(text, next)` then a
unique bare match. A recompiled game binary therefore still matches. Strings
that changed upstream simply fail to match, are reported as a count at the end
of installation, and stay in English; nothing is corrupted.

Dialogue data is written at **fixed length**, space-padded, in place. No size
field anywhere in the nested container format changes, and the archive index
stays byte-identical.

## Safety

Original `Exanima.exe` and `Resource.rpk` are copied to `.orijinal` before the
first install. If a backup is missing and the live file is already patched, the
installer refuses to continue rather than saving a patched file as "original".
Uninstall restores the backups.

Save files are never touched.

---

## Turkce

Exanima'nin tam Turkce cevirisi. Resmi degildir, hayran yapimidir, ucretsizdir.

Yukleyici hazir dosya tasimaz; oyunun kendi dosyalarini okuyup Turkce surumu
sizin bilgisayarinizda uretir. Bu yuzden indirilen dosya kucuktur ve oyun
guncellendiginde programi tekrar calistirmak yeterlidir.

Derlemek icin:

```
pip install pyinstaller
yap.bat
```

Derlemeden calistirmak icin: `python kur.py`

Bu resmi olmayan bir hayran cevirisidir, Bare Mettle Entertainment ile bir
baglantisi yoktur.
