#!/bin/sh
# Ana HTML'i ve dokuları mobil kabuğun www klasörüne kopyalar.
# Kaynak her zaman ../uzay-macerasi.html — www içini elle düzenleme.
set -e
cd "$(dirname "$0")"
rm -rf www
mkdir -p www
cp ../uzay-macerasi.html www/index.html
mkdir -p www/dokular
cp ../dokular/*.jpg www/dokular/
rm -f www/dokular/_yeni_dunya.jpg
echo "www eşitlendi: $(du -sh www | cut -f1)"
