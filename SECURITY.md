# Security and safety

This project is aimed at young children, so its safety posture is deliberately simple: **the app cannot talk to
anything.**

## What the app does not do

- **No network access.** The HTML contains no `fetch`, `XMLHttpRequest`, `WebSocket`, beacon or external URL.
  The Android manifest declares **no permissions**, so the operating system would block network access even if code
  tried to use it.
- **No storage of personal data.** No accounts, cookies, analytics, advertising or tracking SDKs.
- **No third-party runtime code.** No external scripts; the Android shell contains only Capacitor and a plugin that
  calls the device's built-in text-to-speech engine.
- **No dangerous APIs.** No `eval`, no dynamic code loading, no clipboard, camera, microphone or location access.
- Android `allowBackup` and cleartext traffic are disabled.

Rules for contributions: pull requests that add network access, permissions, analytics, advertising, remote
configuration or third-party runtime code will not be merged.

## Verifying a build

Official builds are published only as **GitHub Releases of this repository** (see the milestone
"Phase D — Stores" and the reproducible-builds issue). Until then, the only trustworthy way to run the app on a phone
is to build it yourself from this source (`mobil/README.md`). An APK obtained from anywhere else may have been
modified and should not be installed.

To check a build you have:

- Compare its SHA-256 with the checksum on the release page.
- Inspect its manifest: `aapt dump permissions app.apk` (or `apkanalyzer manifest print app.apk`) must list **no Android
  system permissions**. The only entry is the app's own internal `tr.uzaymacerasi.app.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION`,
  a signature-level marker that AndroidX adds automatically; it grants nothing.

## Reporting a problem

If you find anything that could harm a device, leak data or mislead a child or parent, please open an issue in this
repository. If the problem is sensitive, use GitHub's private vulnerability reporting on the Security tab instead.
