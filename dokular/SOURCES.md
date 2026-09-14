# Surface textures — sources and licences

The 19 surface maps in this folder are used by `uzay-macerasi.html` as planet and moon surfaces in the 3D view. All
are **2048×1024 equirectangular** maps, JPEG quality 72. There is also a **sky panorama**, `samanyolu.jpg`
(4096×2048, see below). About 11 MB in total.

**If a file is deleted, that body falls back to a procedurally generated texture** — the app keeps working.

---

## Solar System Scope — CC BY 4.0

<https://www.solarsystemscope.com/textures/>
Attribution is required; the app shows it in the credit line under the catalog panel.

| File | Source file |
|---|---|
| `merkur.jpg` | 2k_mercury.jpg |
| `venus.jpg` | 2k_venus_atmosphere.jpg (cloud cover — the face seen from outside) |
| `dunya.jpg` | 2k_earth_daymap.jpg |
| `mars.jpg` | 2k_mars.jpg |
| `jupiter.jpg` | 2k_jupiter.jpg |
| `saturn.jpg` | 2k_saturn.jpg |
| `uranus.jpg` | 2k_uranus.jpg |
| `neptun.jpg` | 2k_neptune.jpg |
| `ay.jpg` | 2k_moon.jpg |
| `ceres.jpg` | 2k_ceres_fictional.jpg |
| `eris.jpg` | 2k_eris_fictional.jpg |

**Note:** the Ceres and Eris maps are *artistic* (fictional), not measured data. Ceres's real Dawn maps are either
gridded/labelled or in Mercator projection, so they were not used; Eris has no surface map at all (too far away,
no spacecraft has visited).

## Wikimedia Commons — NASA / JPL / USGS, public domain

| File | Source file |
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

## Deliberately left procedural

Real maps exist for these four bodies, but large parts of their surfaces have never been imaged — the maps have big
black gaps that look like rendering bugs once wrapped onto a sphere. The generated textures are complete, so they
were preferred:

| Body | Reason |
|---|---|
| Enceladus | The available colour map looked false-coloured and broken |
| Triton | Voyager 2 imaged only one hemisphere |
| Charon | The lower half of the New Horizons map is empty |
| Miranda | Voyager 2 imaged only the southern hemisphere |

You can replace them with real maps: drop a 2:1 file with the right name (e.g. `enceladus.jpg`) into this folder and
the app will pick it up automatically.

---

## ESO — CC BY 4.0

| File | Source |
|---|---|
| `samanyolu.jpg` | ESO / S. Brunier, "The Milky Way panorama" (eso0932a) |

<https://www.eso.org/public/images/eso0932a/>

Serge Brunier's real Milky Way panorama. The original is 6000×3000; this copy is downscaled to **4096×2048** and saved
as JPEG 60 (2.1 MB). Attribution is required; the app shows it in the credit line under the catalog panel.
**Do not delete.**

**Frame:** equirectangular in galactic coordinates — the horizontal centre is the galactic centre, the vertical centre
the galactic equator. The app maps `u = 0.5 - l/360°`, `v = 0.5 - b/180°` (longitude increases to the left, the
convention for maps viewed from inside the sphere). **A replacement panorama must use the same frame**, otherwise the
sky shifts or mirrors.

If the file is deleted the sky falls back to a generated Milky Way map — the app keeps working.

### Why not NASA's map

NASA SVS "Deep Star Maps 2020" (<https://svs.gsfc.nasa.gov/4851>, Gaia data, public domain) would be the most accurate
source, but it is only offered as **HDR EXR** (the 4k version is 40 MB) and its JPEG version is 1024×512, too small.
If you can convert it: tone-map `starmap_2020_4k_gal.exr` to a 4096×2048 JPEG and replace `samanyolu.jpg` —
**nothing changes in the code**, because NASA's `_gal` version uses the same galactic equirectangular frame.

---

## Unused file

`_yeni_dunya.jpg` — an alternative, Blue-Marble-style Earth map left over from the texture hunt. The code **does not
load it** (the leading underscore also prevents accidental matching). Swap it with `dunya.jpg` to try it; deleting it
is fine too.
