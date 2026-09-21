# Tools

These two scripts derive and check the scale used inside `uzay-macerasi.html`. The app does not need them to run —
they are for redoing the calculation instead of editing numbers by hand.

## `olcek.py` — size and distance solver

Produces the radius of every body from the Sun to Deimos and the orbital radius of every moon. Three rules:

- **Size:** every body is `E × (R_real / R_Earth)^p`. Currently `E = 0.7021, p = 0.80` (chosen so the Sun comes out at
  30 units). A single curve is essential — with one curve for planets and another for moons, Ceres ends up drawn
  larger than Ganymede.
- **Moon orbits:** the real distance (in planet radii) is compressed with exponent 0.52; the family is pinned to the
  planet's surface at one end and to the system's budget at the other. No moon is ever placed **farther** than its
  real distance.
- **Budget:** neighbouring systems must not overlap; the space is shared max-min fairly (a common reach factor `F`
  is grown by binary search, then systems with room are grown individually). Splitting the gap in half is wrong — tiny
  Ceres would take as much room as half of Jupiter.

```
python3 -c "
import olcek
r,ua,F = olcek.coz(E=0.7021, P=0.80, M=0.52)
print(olcek.denetle(r,ua) or 'no errors')
print({k:round(v,3) for k,v in r.items()}); print({k:round(v,2) for k,v in ua.items()})"
```

Raising `p` brings the ratios closer to reality but shrinks the planets (at 0.85 Earth goes 0.70 → 0.56, Mercury
0.33 → 0.25). If you change it, write **all** resulting `r` and `a` values into the HTML together.

## `denetle.py` — data check

Reads the HTML and compares orbital periods, eccentricities, inclinations, axial tilts, rotation directions and moon
periods with real values.

```
cd araclar && python3 denetle.py
```

Expected output: only the `EKSEN eris` warning. Eris's pole orientation has genuinely never been measured — that
warning is left on purpose; do not silence it with an invented number.

## `ikon.svg` and `ikon-png.sh`

`ikon.svg` is the launcher icon: Ganymede, the moon the app is named after, in front of Jupiter. It is the single
source for the artwork. The Android adaptive icon
(`mobil/android/app/src/main/res/drawable/ic_launcher_foreground.xml`) carries the same path data by hand — change
one and you must change the other.

`sh araclar/ikon-png.sh` regenerates the legacy PNG launcher icons (Android 7.x only; 8.0 and later use the
adaptive icon). It crops the central 72 of the 108 canvas, scales it to fill, lays it over the background colour
and masks it — a rounded square for `ic_launcher.png`, a circle for `ic_launcher_round.png` — at all five
densities. It needs nothing but Chrome, which is already required to test the app.
