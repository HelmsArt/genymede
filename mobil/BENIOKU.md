# Uzay Macerası — Android/iOS kabuğu

> Paketleme ve derleme belgesi. Açık işler depo Issues sayfasında.

Bu klasör, `../uzay-macerasi.html` dosyasını Capacitor ile mobil uygulamaya sarar.
**Uygulamanın kaynağı hâlâ ana klasördeki tek HTML dosyasıdır**; burada oyun kodu yok,
yalnız paketleme var. `www/` klasörü her derlemede sıfırdan üretilir, içini elle düzenleme.

## Bir kez kurulacaklar (macOS + Homebrew örneği)

| Ne | Nerede | Nasıl kuruldu |
|---|---|---|
| Node 24 | nvm | zaten vardı |
| JDK 21 | `/opt/homebrew/opt/openjdk@21` | `brew install openjdk@21` (Capacitor 8 tam olarak 21 ister) |
| Android SDK | `/opt/homebrew/share/android-commandlinetools` | `brew install --cask android-commandlinetools` + `sdkmanager` ile platform 35/36, build-tools, platform-tools, emulator |
| Öykünücü | AVD adı `UzayTablet` (Pixel Tablet, Android 15) | `avdmanager create avd` |

SDK yolu `android/local.properties` içinde (git'e girmez; yoksa `sdk.dir=...` satırıyla oluştur ya da `ANDROID_HOME` yeter).
Java'yı `ortam.sh` bulur; projede makineye özel yol yok.

## Her seferinde: HTML'i değiştirdin, telefonda görmek istiyorsun

```sh
cd mobil
npm install          # ilk seferde
npm run android      # ortam.sh → esitle.sh → cap sync → gradlew assembleDebug → UzayMacerasi-debug.apk
npm run yukle        # bağlı telefona / açık öykünücüye kurar
npm run oykunucu     # UzayTablet öykünücüsünü -gpu host ile açar
```

`ortam.sh` JDK 21 ve Android SDK'yı bilinen yerlerde arar (Homebrew, Android Studio); makineye özel yol projede yazılı değil.
Elle komut çalıştıracaksan önce `. ./ortam.sh`.

Telefonda: Ayarlar → Geliştirici seçenekleri → USB hata ayıklama açık olmalı; ilk bağlantıda
telefon "bu bilgisayara güven" diye sorar. `adb devices` cihazı listelemeli.

Öykünücüyü açmak: `npm run oykunucu` (= `emulator -avd UzayTablet -gpu host`) — **`-gpu host` şart.** Varsayılan ayarla
öykünücü GPU'yu yazılımla taklit ediyor (SwiftShader) ve Güneş Sistemi bile 5 kare/sn'ye düşüyor;
o sayı uygulamayı değil öykünücüyü ölçer. `-gpu host` ile Mac'in GPU'su kullanılır, 60 kare/sn.

APK'yı elle dağıtmak: `UzayMacerasi-debug.apk` dosyasını telefona gönder (WhatsApp, Drive…),
telefonda dokun, "bilinmeyen kaynaklara izin ver" de. Debug imzalı; mağazaya bu gitmez.

## Yapılan Android ayarları

- `AndroidManifest.xml`: `screenOrientation="sensorLandscape"` — uygulama yatay çalışır
  (üst çubuk 7 sekme + 4 düğme dikey telefona sığmıyor).
- `styles.xml`: tam ekran (`windowFullscreen`), çentik alanına yayılma (`shortEdges`),
  durum ve gezinme çubuğu uzay rengi `#070620`.
- İkon: `res/drawable/ic_launcher_foreground.xml` vektör (halkalı gezegen), arka plan `#150C33`.
  Eski Android (API 24-25) için PNG'ler `mipmap-*/ic_launcher*.png` — Chrome headless ile
  `ikon.html`'den üretildi, aynı çizim.
- Açılış ekranı: `res/drawable/splash.xml` — koyu zemin + ortada ikon. Capacitor'ın
  varsayılan `splash.png`'leri silindi.
- **Sesli anlatım:** Android WebView'da `speechSynthesis` **yok** (tarayıcıdan farklı). Bu yüzden
  `@capacitor-community/text-to-speech` eklentisi kurulu; HTML'deki `konus()`/`sesiKes()` önce
  `Capacitor.Plugins.TextToSpeech` var mı bakar (`yerelOkuyucu()`), yoksa tarayıcı yoluna düşer.
  Öykünücüde `tr-TR` sesi doğrulandı. Eklenti `npm install` ile gelir, `cap sync` Android'e bağlar.
- `capacitor.config.json`: `androidScheme: https` (WebView `https://localhost` altında çalışır;
  `speechSynthesis`, worker ve `fetch` için güvenli bağlam sağlar).

## HTML tarafında mobil için yapılanlar (15 Eylül 2026)

- `<meta name="viewport" … viewport-fit=cover>` eklendi — yoksa sayfa masaüstü genişliğinde açılıp küçülüyordu.
- Üst/alt çubuklara `env(safe-area-inset-*)` payı.
- `@media (pointer: coarse)`: düğmeler en az 42 px, hover kayması kapalı, kaydıraç tutamağı iri.
- **İki parmakla sürükleme = kaydırma** (masaüstündeki sağ tık). Kıstırma yakınlaştırmaya ek olarak
  aynı olayda çalışır; `ortaX/ortaY` iki parmağın orta noktasını izler.

## Telefonda ölçüm — tanı penceresi dokunmatikte

- **Roket rozetine (🚀, sol üst) 5 kez hızlı dokun** → Shift+D tanı penceresi açılır/kapanır.
- **Tanı açıkken roketi ~1 sn basılı tut** → WebGL yolu elle kapanır (harita + worker yolu), tekrar basılı tut → geri açılır.
  Klavyede karşılığı **Shift+G**. Pencere "WebGL ELLE KAPATILDI" yazar.
- Bakılacak satırlar: `fps`, `worker: N adet`, `son hesap … ms`, `ekranda ×k` (1,00 keskin demek).
- Katalog açıkken pencere kataloğun sağına kayar.

## Açık işler

Mobil kabukla ilgili açık işler depo Issues sayfasında `mobil` etiketiyle duruyor.
