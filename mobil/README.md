# Genymede — Android / iOS shell

> Packaging and build notes. Open work is on the repository's Issues page.

This folder wraps `../uzay-macerasi.html` into a mobile app with Capacitor. **The application source is still the
single HTML file in the parent folder**; there is no game code here, only packaging. The `www/` folder is regenerated
on every build — do not edit it.

## One-time setup (macOS + Homebrew example)

| What | Where | How |
|---|---|---|
| Node 22+ | nvm | Capacitor 8 requires it |
| JDK 21 | `/opt/homebrew/opt/openjdk@21` | `brew install openjdk@21` (Capacitor 8 requires exactly 21) |
| Android SDK | `/opt/homebrew/share/android-commandlinetools` | `brew install --cask android-commandlinetools`, then `sdkmanager` for platforms 35/36, build-tools, platform-tools, emulator |
| Emulator (optional) | AVD `UzayTablet` (Pixel Tablet, Android 15) | `avdmanager create avd` |

The SDK path lives in `android/local.properties` (not committed; create it with `sdk.dir=...` or set `ANDROID_HOME`).
`ortam.sh` locates the JDK and SDK in the usual places (Homebrew, Android Studio); no machine-specific path is stored
in the project.

## Every time: you changed the HTML and want it on a phone

```sh
cd mobil
npm install          # first time only
npm run android      # ortam.sh → esitle.sh → cap sync → gradlew assembleDebug → UzayMacerasi-debug.apk
npm run yukle        # installs on a connected phone / running emulator
npm run oykunucu     # starts the UzayTablet emulator with -gpu host
```

For manual commands run `. ./ortam.sh` first.

On the phone: Settings → Developer options → USB debugging must be on; on first connection the phone asks you to trust
the computer. `adb devices` must list it.

Emulator: **`-gpu host` is required.** With the default setting the emulator emulates the GPU in software
(SwiftShader) and even the Solar System drops to 5 fps — that number measures the emulator, not the app. With
`-gpu host` the Mac's GPU is used and the app runs at 60 fps.

The debug APK is signed with a debug key and is for your own testing only; it is not what goes to the store.

## Android settings applied

- `AndroidManifest.xml`: **no permissions** (Capacitor's default `INTERNET` permission was removed — the app is fully
  offline), `allowBackup="false"`, `usesCleartextTraffic="false"`, `screenOrientation="sensorLandscape"`
  (the top bar with 7 tabs + 4 buttons does not fit a portrait phone).
- `MainActivity.java`: immersive full screen (system bars hidden, shown transiently by swipe).
- `styles.xml`: full screen, `shortEdges` cutout mode, status/navigation bar colour `#070620`.
- Icon: `res/drawable/ic_launcher_foreground.xml`, a vector ringed planet on a `#150C33` background. PNG fallbacks
  for API 24–25 in `mipmap-*/ic_launcher*.png`, same drawing.
- Splash: `res/drawable/splash.xml`, dark background with the icon centred. Capacitor's default `splash.png` files were removed.
- **Narration:** Android's WebView has **no** `speechSynthesis`. The `@capacitor-community/text-to-speech` plugin is
  installed; the HTML's `konus()` / `sesiKes()` first look for `Capacitor.Plugins.TextToSpeech` (`yerelOkuyucu()`) and
  fall back to the browser API otherwise. Verified with the `tr-TR` voice.
- **Back button:** the `@capacitor/app` plugin is installed so the hardware back key closes one layer at a time —
  planet maker, then any open sheet, then the info card, then the game — and only leaves the app once nothing is
  open. The HTML registers the listener in `geriTusuKur()` and shares the ordering with the Escape key through
  `geriGit()`. Registering a `backButton` listener makes the page responsible for quitting, hence the `exitApp()`
  call at the end of the chain. The plugin declares no Android permissions and has no dependencies of its own.
- `capacitor.config.json`: `androidScheme: https` (the WebView serves from `https://localhost`, giving a secure
  context for workers).

## Mobile-specific changes in the HTML

- `<meta name="viewport" … viewport-fit=cover>`; safe-area insets on the top and bottom bars.
- `@media (pointer: coarse)`: buttons at least 42 px tall, no hover lift, larger slider thumbs.
- **Two-finger drag = pan** (the desktop right-drag), in the same handler as pinch-zoom.

## Diagnostics on a touch screen

- **Tap the rocket badge (🚀, top left) 5 times quickly** → the Shift+D diagnostics overlay toggles.
- **With diagnostics open, long-press the rocket (~1 s)** → the WebGL path is switched off (map + worker path);
  long-press again to switch it back. Keyboard equivalent: **Shift+G**.
- Lines to read: `fps`, `worker: N adet` (worker count), `son hesap … ms` (last map computation),
  `ekranda ×k` (on-screen magnification; 1.00 means pixel-sharp).
