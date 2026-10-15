<div align="center">
  <img src="new-icons/arcadeia.png" alt="Arcadeia" width="112" />
  <h1>Arcadeia</h1>
  <p><strong>Your retro game library, ready to play.</strong><br />
  An open-source Android frontend for Libretro and standalone emulators.</p>
  <p><strong>Android · Kotlin · Jetpack Compose · GPL-3.0</strong><br />
  Arcadeia blue: <code>#2766B0</code></p>
</div>

<table align="center">
  <tr>
    <td width="33%"><img src="docs/screenshots/dashboard.jpg" alt="Arcadeia dashboard with a featured game, library totals, and unplayed games" /></td>
    <td width="33%"><img src="docs/screenshots/library.jpg" alt="Arcadeia game library with cover art and filters" /></td>
    <td width="33%"><img src="docs/screenshots/settings.jpg" alt="Arcadeia appearance and settings" /></td>
  </tr>
  <tr>
    <td align="center"><sub>Dashboard</sub></td>
    <td align="center"><sub>Library</sub></td>
    <td align="center"><sub>Settings</sub></td>
  </tr>
</table>

## Features

- **Folder-aware library** — identifies systems from ROM folder names before file metadata, then organizes games into systems, favorites, collections, and recent-play lists. Folder aliases follow [ES-DE](https://es-de.org/) conventions.
- **Unified discovery** — searches and combines game entries from [IGDB](https://api-docs.igdb.com/), [ScreenScraper](https://www.screenscraper.fr/), and [TheGamesDB](https://thegamesdb.net/). Provider credentials, approval, or proxy setup may be required.
- **External emulators** — launch compatible games or find official releases for supported emulator apps:

  | System | Emulator | Official releases |
  | --- | --- | --- |
  | PlayStation 2 | [ARMSX2](https://github.com/ARMSX2/ARMSX2), [NetherSX2 Classic](https://github.com/Trixarian/NetherSX2-classic) | [ARMSX2](https://github.com/ARMSX2/ARMSX2/releases) · [NetherSX2](https://github.com/Trixarian/NetherSX2-classic/releases) |
  | Nintendo Switch | [Eden](https://git.eden-emu.dev/eden-emu/eden) | [Eden](https://git.eden-emu.dev/eden-emu/eden/releases) |
  | Nintendo 3DS | [Azahar](https://github.com/azahar-emu/azahar) | [Azahar](https://github.com/azahar-emu/azahar/releases) |

  Arcadeia checks release compatibility and opens Android's installer for confirmation.
- **Play your way** — Libretro cores, save states, autosaves, optional cloud sync, touch and gamepad controls, and Android TV support.
- **Portable save vault** — keep exported Eden save archives and PS2 memory cards together; restore them through the emulator's own import flow.
- **Expressive design** — adaptive Material 3, dynamic color options, and a pure-black AMOLED theme.

## Supported systems

**Libretro:** Atari 2600, 7800 and Lynx; NES; SNES; Game Boy, Color and Advance; Genesis and Sega CD; Master System; Game Gear; Nintendo 64; PlayStation; PSP; Nintendo DS; Arcade (FinalBurn Neo and MAME 2003 Plus); PC Engine; Neo Geo Pocket and Color; WonderSwan and Color; DOS; Nintendo 3DS with a compatible Citra core.

PlayStation 2 and Nintendo Switch use compatible external emulator apps listed above. Available cores and formats depend on the app build and device.

Arcadeia does not include ROM or BIOS files.

## Build

With the Android SDK and JDK configured:

```sh
./gradlew :arcadeia-app:assembleFreeDynamicDebug
```

## Credits

Arcadeia is a fork of [Lemuroid](https://github.com/Swordfish90/Lemuroid) and integrates [LibretroDroid](https://github.com/Swordfish90/LibretroDroid). The folder model references [ES-DE](https://es-de.org/); UI studies include [PixelMusic](https://github.com/Xing1P/PixelMusic) and [PixelPlayer](https://github.com/PixelPlayerHQ/PixelPlayer).

Arcadeia is licensed under [GPL-3.0](COPYING). Third-party notices and licenses are in [`licenses/`](licenses/).
