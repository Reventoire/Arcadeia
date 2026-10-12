# Arcadeia application identity

## Decision and audit

Android's installed application ID is separate from the Kotlin namespace:
https://developer.android.com/build/configure-app-module

| Dependency | Decision |
| --- | --- |
| Installed package | `io.github.reventoire.arcadeia`; debug adds `.debug` |
| Kotlin namespace, generated R/BuildConfig imports, Dagger, manifest class names | Keep `com.swordfish.lemuroid`; avoid a large refactor unrelated to installation |
| Flavor IDs | Free/play and bundle/dynamic share the release ID; these variants replace each other, while debug and upstream coexist |
| Labels | Arcadeia / Arcadeia Debug; retain resource key `lemuroid_name` for existing callers |
| Phone launcher | New geometric Arcadeia mark, API 23 vector fallback, adaptive and monochrome art |
| Android TV | New 320x180 xhdpi banner and bitmap channel logo; channel label already uses app label |
| Deep links | `arcadeia://<installed-package>/play-game/id/<id>` and `/open-leanback`; generated game intents are package-scoped |
| Exported game entry | Validate scheme, installed-package host, exact route and numeric ID before loading; invalid/missing IDs display the existing error UI |
| Providers | Existing `${applicationId}.androidx-startup` placeholder is isolated; retained removal declaration is unchanged |
| Processes | `:game` is package-relative and isolated; main-process detection already uses runtime package name |
| Storage | Room, preferences, WorkManager, internal cores/system files use app context; saves, states and previews use app-specific external storage |
| ROM access | User-selected SAF directories may contain the same ROMs; URI permissions must be granted to Arcadeia separately |
| Shortcuts / TV programs | Producers call `DeepLink`; recreate them in Arcadeia, since old links target Lemuroid |
| Benchmarks | Retarget release package, leaving class descriptors and baseline profile namespace intact |
| Signing | Independent environment-configured release key; standard local debug signing, no upstream signing password defaults |
| Google Drive | API application name uses runtime package; new OAuth configuration is required outside source |
| Play dynamic cores / reviews | Keep module names; new Play listing and delivery configuration required before claiming Play support |
| Core and PPSSPP assets | Keep pinned upstream LemuroidCores endpoints and submodule names; changing them would break downloads |
| License / attribution | Preserve COPYING, source copyright headers and raw/licenses.html; explicitly credit Lemuroid/Retrograde/LibretroDroid in README |
| Historical assets | Retain unused upstream artwork/screenshots and upstream funding links as provenance; no upstream store badges represent Arcadeia |

The application ID is a proposed permanent identity based on the repository owner's
GitHub handle. Confirm its availability in your intended distribution account before
publishing. After publication, keep both this ID and the release signing key stable.
This patch does not migrate installed Lemuroid data. Any APK from this fork previously
installed as `com.swordfish.lemuroid` remains a separate old installation. Export/copy
saves deliberately; do not uninstall or clear its data as part of this migration.

## Build and signing

Use JDK 17, SDK 35 and build tools 34.0.0, with network access for dependencies:

```sh
git submodule update --init --recursive
python3 scripts/check_application_identity.py
./gradlew :lemuroid-app:assembleFreeDynamicDebug :lemuroid-app:lintFreeDynamicDebug
./gradlew :lemuroid-app:assembleFreeDynamicRelease
```

FreeDynamic is the initial independent-install target: it downloads the existing
pinned cores from GitHub. Test FreeBundle too when bundled core artifacts are available.
With no signing environment variables, release output is **unsigned**. No key or secret
is created or registered by this patch. Supply all four variables to sign a release:

- `ARCADEIA_KEYSTORE_PATH`: path to your own keystore
- `ARCADEIA_KEY_ALIAS`
- `ARCADEIA_STORE_PASSWORD`
- `ARCADEIA_KEY_PASSWORD`

Partial configuration fails instead of falling back to upstream credentials. The tag
publish workflow additionally needs `ARCADEIA_RELEASE_KEYSTORE_BASE64` (base64 keystore)
and the three key/password secrets above. It removes the temporary keystore even on
failure. Existing upstream `RELEASE_KEYSTORE` secrets are deliberately not reused.

Before distribution verify the certificate with `apksigner verify --print-certs`.
Signing certificates for debug, sideloaded release and Play app signing may differ.
Google OAuth requires registering the **installed package plus certificate SHA-1**:
https://developers.google.com/identity/sign-in/android/legacy-gsi-start
Use a separate Arcadeia Google Cloud/OAuth project with Drive app-data authorization
and an Arcadeia Play Console entry. Changing the Drive API application-name string
alone neither configures OAuth nor guarantees cloud-data isolation. Until that setup
and sync tests pass, use Free variants and do not advertise Arcadeia cloud sync.

## APK checks

```sh
python3 scripts/verify_apk_identity.py /path/to/aapt \
  lemuroid-app/build/outputs/apk/freeDynamic/debug/lemuroid-app-free-dynamic-debug.apk \
  io.github.reventoire.arcadeia.debug 'Arcadeia Debug'
```

Repeat for a signed release with `io.github.reventoire.arcadeia` and `Arcadeia`.
Inspect `apkanalyzer manifest print APK` for resolved component classes, the package,
both deep-link filters and all merged provider authorities. No authority or shared UID
may target `com.swordfish.lemuroid`. This merged-manifest check includes dependencies
that source-only checks cannot cover. Verify launcher art on API 23, adaptive icons on
API 26+, themed icons on API 33+, and the Android TV banner/channel icon.

## Android device acceptance (not yet executed)

Use a device or emulator with network access and a legally usable homebrew/test ROM.
Keep an existing Lemuroid install and its data intact. Install Arcadeia with
`adb install -r APK`, then record device/API, APK hash, flavor and certificate.
For the commands below set `APP` to the installed release or debug ID.

```sh
APP=io.github.reventoire.arcadeia.debug
adb shell pm list packages io.github.reventoire.arcadeia
adb shell pm list packages com.swordfish.lemuroid
adb shell dumpsys package "$APP"
adb shell dumpsys package com.swordfish.lemuroid
adb shell am start -W -n "$APP/com.swordfish.lemuroid.app.mobile.feature.main.MainActivity"
```

Expected: both apps remain installed with distinct UIDs/data directories. Arcadeia
launches into its own onboarding, shows its label/art, and Lemuroid remains usable.
Grant Arcadeia its own ROM-directory permission and wait for indexing to finish.

| Test | Expected result |
| --- | --- |
| Launch indexed test ROM from library | Core installs/downloads and game runs; sound, touch controls and gamepad work |
| Save / quick-save / quit / relaunch | Save and state restore in Arcadeia; original app's saves remain unchanged |
| Relaunch after force-stop and device reboot | Library/preferences persist; main and `:game` processes start correctly |
| Link to a valid Arcadeia database game ID | Opens that game in Arcadeia; record actual ID, do not assume `1` exists |
| Invalid, missing, nonnumeric or overflowing game ID, explicit component | Shows error/finishes without crashing or starting a game |
| Wrong host or old scheme, explicit game component | Rejected without querying/loading another game's data |
| Upstream Lemuroid link | Still resolves to Lemuroid, never Arcadeia |
| Debug vs release links | Resolve only to the matching package; IDs refer to separate local databases |
| Shortcut / notification / TV recommendation | Launches the correct installed Arcadeia variant |
| `/open-leanback` on Android TV | Opens Arcadeia TV UI; test recommendations after playing a game |
| Distinct preferences and ROM permissions | Changing Arcadeia settings leaves Lemuroid untouched; neither inherits the other's SAF grants |
| Save/state isolation | Same ROM in both apps writes separate app-specific external directories |
| Factory reset inside Arcadeia | Its existing documented reset behavior applies; Lemuroid remains unchanged |
| Release update signed with same Arcadeia key | Installs as an update and preserves Arcadeia data |

Deep-link commands (replace `42` with a real indexed ID):

```sh
adb shell cmd package resolve-activity --brief -a android.intent.action.VIEW \
  -c android.intent.category.DEFAULT -d "arcadeia://$APP/play-game/id/42"
adb shell am start -W -a android.intent.action.VIEW \
  -d "arcadeia://$APP/play-game/id/42"
adb shell am start -W -a android.intent.action.VIEW \
  -d "arcadeia://$APP/open-leanback"
adb shell am start -W -n "$APP/com.swordfish.lemuroid.app.shared.game.ExternalGameLauncherActivity" \
  -d "arcadeia://$APP/play-game/id/not-a-number"
```

For negative resolution, use `cmd package resolve-activity ... -p "$APP"` with the
upstream scheme/host and expect no matching Arcadeia activity. Also test BROWSABLE
resolution. Capture logcat for launch/core crashes; check native-library loading for
at least one representative 2D system and a supported 3D system. A new application ID
alone cannot prove every emulator core works on every ABI/device.

For **debuggable** builds, `adb shell run-as "$APP" pwd` should report that package's
private directory. Inspect `/sdcard/Android/data/$APP/files/{saves,states}` where the
OS permits it. Use in-app inspection on OS versions restricting shell access. Do not
use `pm clear` on the user's original app. Cloud sync isolation and Play-delivered
cores require separate acceptance after external provisioning.

## Results in the implementation environment

- Base inspected: `93e321d08f3dc0776bb0545da975d2cd7cd1f78f` on `master`.
- Source identity/resource XML regression checks: passed.
- Whitespace/diff checks: passed.
- JDK 17 available.
- Gradle assemble + lint attempted, but wrapper download from services.gradle.org
  failed with `java.net.SocketException: Network is unreachable`, before configuration
  or Kotlin/Android compilation. This is not a successful build.
- No Android SDK, adb or connected Android target available. APK/merged-manifest,
  certificate, side-by-side install, game, deep-link and data-isolation checks remain
  unverified. No production key, OAuth project or Play listing was provisioned.
