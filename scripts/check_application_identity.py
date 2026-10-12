#!/usr/bin/env python3
"""Source identity regression checks; does not replace merged-manifest/device checks."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / 'lemuroid-app'
ANDROID = '{http://schemas.android.com/apk/res/android}'

def read(path):
    return (ROOT / path).read_text()

gradle = read('lemuroid-app/build.gradle.kts')
assert 'applicationId = "io.github.reventoire.arcadeia"' in gradle
assert 'namespace = "com.swordfish.lemuroid"' in gradle
assert 'applicationIdSuffix = ".debug"' in gradle
assert '"lemuroid_name", "Arcadeia"' in gradle
assert '"lemuroid_name", "Arcadeia Debug"' in gradle
assert 'ARCADEIA_KEYSTORE_PATH' in gradle
assert 'keyAlias = "lemuroid"' not in gradle
assert 'debug.keystore' not in gradle

manifest = ET.parse(APP / 'src/main/AndroidManifest.xml').getroot()
application = manifest.find('application')
assert application.get(ANDROID + 'name') == 'com.swordfish.lemuroid.app.LemuroidApplication'
for attr, expected in [('icon', '@mipmap/arcadeia_launcher'),
                       ('roundIcon', '@mipmap/arcadeia_launcher_round'),
                       ('banner', '@mipmap/arcadeia_banner'),
                       ('label', '@string/lemuroid_name')]:
    assert application.get(ANDROID + attr) == expected
links = list(application.iter('data'))
assert len(links) == 2
for link in links:
    assert link.get(ANDROID + 'scheme') == 'arcadeia'
    assert link.get(ANDROID + 'host') == '${applicationId}'
for provider in application.iter('provider'):
    assert '${applicationId}' in provider.get(ANDROID + 'authorities')
assert manifest.get(ANDROID + 'sharedUserId') is None

java = 'lemuroid-app/src/main/java/com/swordfish/lemuroid/app/'
links_source = read(java + 'shared/deeplink/DeepLink.kt')
assert links_source.count('arcadeia://${appContext.packageName}') == 2
assert '.setPackage(appContext.packageName)' in links_source
launcher = read(java + 'shared/game/ExternalGameLauncherActivity.kt')
assert 'toIntOrNull()' in launcher and 'uri.host != packageName' in launcher
for name in ['BaselineProfileGenerator', 'StartupBenchmarks']:
    s = read(f'baselineprofile/src/main/java/com/swordfish/lemuroid/baselineprofile/{name}.kt')
    assert 'packageName = "io.github.reventoire.arcadeia"' in s

# Parse every app resource XML, including translations and new adaptive/vector icons.
xmls = list((APP / 'src/main/res').rglob('*.xml'))
for path in xmls:
    ET.parse(path)
for path in (APP / 'src/main/res').glob('values*/strings.xml'):
    assert 'Lemuroid' not in path.read_text(), path
for name in ['arcadeia_launcher', 'arcadeia_launcher_round']:
    for qualifier in ['mipmap-anydpi', 'mipmap-anydpi-v26']:
        assert (APP / f'src/main/res/{qualifier}/{name}.xml').exists()
assert (ROOT / 'COPYING').exists()
assert (APP / 'src/main/res/raw/licenses.html').exists()
assert '[Lemuroid](https://github.com/Swordfish90/Lemuroid)' in read('README.md')
assert 'get-it-on.png' not in read('README.md')
assert 'ARCADEIA_RELEASE_KEYSTORE_BASE64' in read('.github/workflows/publish.yml')
print(f'PASS: Arcadeia source identity and {len(xmls)} resource XML files')
