# Arcadeia

Arcadeia is an independently installable Android emulator fork of
[Lemuroid](https://github.com/Swordfish90/Lemuroid), based on Libretro.
It retains the existing emulator functionality while using its own Android identity.

- Release ID: `io.github.reventoire.arcadeia`
- Debug ID: `io.github.reventoire.arcadeia.debug`
- Source and project updates: https://github.com/Reventoire/Arcadeia
- No Arcadeia Play Store or F-Droid listing is established by this repository.
  The upstream listings distribute Lemuroid, not Arcadeia.

See [identity, build and device verification](docs/application-identity.md).

## Attribution and license

Arcadeia derives from Lemuroid by Swordfish90 and its contributors, which originated
from [Retrograde](https://github.com/retrograde/retrograde-android) and integrates
[LibretroDroid](https://github.com/Swordfish90/LibretroDroid) and Libretro cores.
The existing [GPL license](COPYING), source copyright notices and
[in-app third-party notices](lemuroid-app/src/main/res/raw/licenses.html) are preserved.
Distribute corresponding source with binary releases as required by the applicable
licenses; emulator cores and dependencies retain their own notices and terms.

The identity migration changes installed IDs, links, signing configuration and
product branding. Internal Kotlin packages and emulator/core module names remain
upstream-compatible. Upstream screenshots under `fastlane` are historical references,
not verified Arcadeia release screenshots.

### Supported Systems:
- Atari 2600 (A26) ([stella](https://docs.libretro.com/library/stella/))
- Atari 7800 (A78) ([prosystem](https://docs.libretro.com/library/prosystem/))
- Atari Lynx (Lynx) ([handy](https://docs.libretro.com/library/handy/))
- Nintendo (NES) ([fceumm](https://docs.libretro.com/library/fceumm/))
- Super Nintendo (SNES) ([snes9x](https://docs.libretro.com/library/snes9x/))
- Game Boy (GB) ([gambatte](https://docs.libretro.com/library/gambatte/))
- Game Boy Color (GBC) ([gambatte](https://docs.libretro.com/library/gambatte/))
- Game Boy Advance (GBA) ([mgba](https://docs.libretro.com/library/mgba/))
- Sega Genesis (aka Megadrive) ([genesis_plus_gx](https://docs.libretro.com/library/genesis_plus_gx/))
- Sega CD (aka Mega CD) ([genesis_plus_gx](https://docs.libretro.com/library/genesis_plus_gx/))
- Sega Master System (SMS) ([genesis_plus_gx](https://docs.libretro.com/library/genesis_plus_gx/))
- Sega Game Gear (GG) ([genesis_plus_gx](https://docs.libretro.com/library/genesis_plus_gx/))
- Nintendo 64 (N64) ([mupen64plus](https://docs.libretro.com/library/mupen64plus/))
- PlayStation (PSX) ([PCSX-ReARMed](https://docs.libretro.com/library/pcsx_rearmed/))
- PlayStation Portable (PSP) ([ppsspp](https://docs.libretro.com/library/ppsspp/))
- FinalBurn Neo (Arcade) ([fbneo](https://github.com/libretro/FBNeo/))
- Nintendo DS (NDS) ([desmume](https://docs.libretro.com/library/desmume/)/[MelonDS](https://docs.libretro.com/library/melonds/))
- NEC PC Engine (PCE) ([beetle_pce_fast](https://docs.libretro.com/library/beetle_pce_fast/))
- Neo Geo Pocket (NGP) ([mednafen_ngp](https://docs.libretro.com/library/beetle_neopop/))
- Neo Geo Pocket Color (NGC) ([mednafen_ngp](https://docs.libretro.com/library/beetle_neopop/))
- WonderSwan (WS) ([beetle_cygne](https://docs.libretro.com/library/beetle_cygne/))
- WonderSwan Color (WSC) ([beetle_cygne](https://docs.libretro.com/library/beetle_cygne/))
- Nintendo 3DS (3DS) ([citra](https://docs.libretro.com/library/citra/))

### Features:
- Android TV support
- Automatically save and restore game states.
- ROMs scanning and indexing
- Optimized touch controls
- Quick save/load
- Support for Zipped ROMs
- Display simulation (LCD/CRT)
- Gamepad support
- Local multiplayer
- Tilt input
- Customizable touch controls (size and position)
- Cloud save sync
- HD mode

### Translations

Arcadeia translations live in the Android string resources. Existing translations
are inherited from Lemuroid; product-name substitutions need native-speaker review.
The upstream Crowdin project belongs to Lemuroid.
