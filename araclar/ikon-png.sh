#!/bin/sh
# Renders the legacy launcher PNGs from araclar/ikon.svg.
#
# Android 8+ uses the adaptive icon (the VectorDrawable foreground plus a solid
# background colour), so these PNGs only matter on API 24-25. They are produced
# the way Android Studio produces legacy icons from an adaptive one: the central
# 72 of the 108 canvas is cropped and scaled to fill, over the background colour,
# then masked - a rounded square for ic_launcher.png, a circle for
# ic_launcher_round.png.
#
# Needs only Chrome, which is already required to test the app. No image
# libraries, no downloads.
set -e
cd "$(dirname "$0")/.."

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "Chrome not found at $CHROME"; exit 1; }

SVG="araclar/ikon.svg"
RES="mobil/android/app/src/main/res"
ZEMIN="#150C33"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

uret() {   # uret <size> <radius-css> <outfile>
  BOY=$1; YARICAP=$2; CIKTI=$3
  python3 - "$SVG" "$BOY" "$YARICAP" "$ZEMIN" > "$TMP/i.html" <<'PY'
import sys, io
svg, boy, yaricap, zemin = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
icerik = io.open(svg, encoding='utf-8').read()
icerik = icerik[icerik.index('<svg'):]          # XML bildirimi ve yorumlar gitsin
olcek = boy * 108.0 / 72.0                      # merkezdeki 72 birim tuvali doldursun
kayma = -boy * 18.0 / 72.0
print(u'''<!doctype html><meta charset="utf-8"><style>
html,body{margin:0;padding:0;background:transparent}
.k{width:%(boy)dpx;height:%(boy)dpx;background:%(zemin)s;border-radius:%(yaricap)s;overflow:hidden;position:relative}
.k svg{position:absolute;left:%(kayma).3fpx;top:%(kayma).3fpx;width:%(olcek).3fpx;height:%(olcek).3fpx}
</style><div class="k">%(svg)s</div>''' % dict(boy=boy, zemin=zemin, yaricap=yaricap,
                                               kayma=kayma, olcek=olcek, svg=icerik))
PY
  "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
    --force-device-scale-factor=1 --default-background-color=00000000 \
    --virtual-time-budget=3000 --window-size=$BOY,$BOY \
    --screenshot="$TMP/o.png" "$TMP/i.html" >/dev/null 2>&1
  [ -f "$TMP/o.png" ] || { echo "Chrome produced no image for $CIKTI"; exit 1; }
  mv "$TMP/o.png" "$CIKTI"
  printf '  %-56s %s\n' "$CIKTI" "$(sips -g pixelWidth -g pixelHeight "$CIKTI" | awk '/pixel/{printf "%s ", $2}')"
}

echo "Rendering legacy launcher icons from $SVG"
for p in mdpi:48 hdpi:72 xhdpi:96 xxhdpi:144 xxxhdpi:192; do
  YOGUNLUK=${p%%:*}; BOY=${p##*:}
  uret "$BOY" "22%" "$RES/mipmap-$YOGUNLUK/ic_launcher.png"
  uret "$BOY" "50%" "$RES/mipmap-$YOGUNLUK/ic_launcher_round.png"
done
echo "Done."
