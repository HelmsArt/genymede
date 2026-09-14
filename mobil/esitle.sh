#!/bin/sh
# Copies the main HTML and the textures into the mobile shell's www folder.
# The source is always ../uzay-macerasi.html — never edit www by hand.
set -e
cd "$(dirname "$0")"
rm -rf www
mkdir -p www
cp ../uzay-macerasi.html www/index.html
mkdir -p www/dokular
cp ../dokular/*.jpg www/dokular/
rm -f www/dokular/_yeni_dunya.jpg
echo "www synced: $(du -sh www | cut -f1)"
