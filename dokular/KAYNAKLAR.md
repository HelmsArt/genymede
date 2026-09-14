# Gezegen Yüzey Görselleri — Kaynaklar ve Lisanslar

Bu klasördeki 19 yüzey haritası, `uzay-macerasi.html` tarafından 3B görünümde
gezegen ve uydu yüzeyi olarak kullanılır. Hepsi **2048×1024 eş dikdörtgen
(equirectangular)** harita, JPEG kalite 72.

Bunlara ek olarak bir de **gökyüzü panoraması** var: `samanyolu.jpg`
(4096×2048, aşağıda). Toplam ~11 MB.

**Bir dosya silinirse o cisim kodla üretilen prosedürel dokuya döner** —
program çalışmaya devam eder, hiçbir şey bozulmaz.

---

## Solar System Scope — CC BY 4.0

<https://www.solarsystemscope.com/textures/>
Kullanırken kaynak belirtilmesi gerekir; uygulamada katalog panelinin altında
künye olarak gösteriliyor.

| Dosya | Kaynak dosya |
|---|---|
| `merkur.jpg` | 2k_mercury.jpg |
| `venus.jpg` | 2k_venus_atmosphere.jpg (bulut örtüsü — dışarıdan görünen yüz) |
| `dunya.jpg` | 2k_earth_daymap.jpg |
| `mars.jpg` | 2k_mars.jpg |
| `jupiter.jpg` | 2k_jupiter.jpg |
| `saturn.jpg` | 2k_saturn.jpg |
| `uranus.jpg` | 2k_uranus.jpg |
| `neptun.jpg` | 2k_neptune.jpg |
| `ay.jpg` | 2k_moon.jpg |
| `ceres.jpg` | 2k_ceres_fictional.jpg |
| `eris.jpg` | 2k_eris_fictional.jpg |

**Not:** Ceres ve Eris haritaları *sanatsal* (fictional) — gerçek ölçüm verisi
değil. Ceres'in gerçek Dawn haritaları ya ızgaralı/etiketli ya da Mercator
projeksiyonunda olduğu için kullanılmadı; Eris'in ise hiç yüzey haritası yok
(çok uzak, hiçbir araç yakınından geçmedi).

## Wikimedia Commons — NASA / JPL / USGS, kamu malı

| Dosya | Kaynak dosya |
|---|---|
| `pluton.jpg` | Pluto-map-sept-16-2015.jpg (New Horizons) |
| `io.jpg` | Io for GeoHacks.jpg (Galileo/Voyager, USGS) |
| `europa.jpg` | Moon Europa color map.jpg |
| `ganymede.jpg` | Ganymede map NASA JPL Voyager.jpg |
| `callisto.jpg` | Callisto map NASA JPL Voyager.jpg |
| `titan.jpg` | PIA22770 (Cassini) |
| `phobos.jpg` | Phobos Viking Mosaic DLRcontrol 7200.jpg |
| `deimos.jpg` | Deimos color map.jpg |

---

## Bilerek prosedürel bırakılanlar

Bu dört cismin gerçek haritaları var ama yüzeylerinin büyük bölümü hiç
görüntülenmemiş — haritalarda kocaman siyah boşluklar var ve küreye sarılınca
çizim hatası gibi görünüyorlar. Kodla üretilen dokular eksiksiz olduğu için
onlar tercih edildi:

| Cisim | Sebep |
|---|---|
| Enceladus | Elde edilen renkli harita yapay renkli ve bozuk görünüyordu |
| Triton | Voyager 2 yalnız bir yarısını görüntüledi |
| Charon | New Horizons haritasının alt yarısı boş |
| Miranda | Voyager 2 yalnız güney yarımküreyi görüntüledi |

İstersen bunları da gerçek haritalarla değiştirebilirsin: dosyayı bu klasöre
`enceladus.jpg` gibi doğru adla, 2:1 oranında koyman yeterli — program
otomatik olarak onu kullanmaya başlar.

---

## ESO — CC BY 4.0

| Dosya | Kaynak |
|---|---|
| `samanyolu.jpg` | ESO / S. Brunier, "The Milky Way panorama" (eso0932a) |

<https://www.eso.org/public/images/eso0932a/>

Serge Brunier'in çektiği gerçek Samanyolu panoraması. Özgün dosya 6000×3000;
buradaki sürüm **4096×2048**'e küçültülüp JPEG 60 ile kaydedildi (2,1 MB).
Kullanırken kaynak belirtilmesi gerekir; uygulamada katalog panelinin altındaki
künye satırında gösteriliyor. **Silme.**

**Çerçevesi:** galaktik koordinatlarda eş dikdörtgen — yatay ortası galaksi
merkezi, dikey ortası galaktik ekvator. Program şu eşlemeyi kullanır:
`u = 0,5 - l/360°`, `v = 0,5 - b/180°` (boylam sola artar; gökyüzüne içeriden
bakan haritaların kuralı). **Yerine başka bir panorama koyacaksan aynı çerçevede
olmalı**, yoksa gökyüzü kayar ya da aynalanır.

Dosya silinirse gökyüzü kodla üretilen bir Samanyolu haritasına döner —
program çalışmaya devam eder.

### Neden NASA'nın haritası değil

NASA SVS "Deep Star Maps 2020" (<https://svs.gsfc.nasa.gov/4851>, Gaia verisi,
kamu malı) bu iş için en doğru kaynak olurdu, ama yalnızca **HDR EXR** olarak
sunuluyor (4k sürümü 40 MB) ve JPEG sürümü 1024×512 ile fazla düşük. EXR'ı
çevirecek araç elimizde yoktu. İleride çevirebilirsen: `starmap_2020_4k_gal.exr`
sürümünü tonlayıp 4096×2048 JPEG'e çevirip `samanyolu.jpg`in yerine koy —
**kodda hiçbir şey değişmez**, çünkü NASA'nın `_gal` sürümü de aynı galaktik
eş dikdörtgen çerçevededir.

---

## Paylaşırken

Görseller ayrı dosya olduğu için proje artık tek dosya değil.
`uzay-macerasi.html` ile bu klasörü **birlikte** göndermelisin.
Sadece HTML'i gönderirsen program prosedürel dokularla çalışır — bozulmaz,
yalnız gezegenler kodla çizilmiş görünür.

---

## Kullanılmayan dosya

`_yeni_dunya.jpg` — NASA Blue Marble tarzı alternatif bir Dünya haritası. Doku
indirme turundan kalan bir aday; kod onu **çağırmıyor** (alt çizgiyle başladığı
için de kazara eşleşmez). Denemek istersen `dunya.jpg` ile yer değiştir.
Silinmesinde de sakınca yok.
