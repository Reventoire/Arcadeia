#!/usr/bin/env python3
"""Check an actual APK's installed package and resolved labels using SDK aapt."""
import re
import subprocess
import sys

if len(sys.argv) != 5:
    sys.exit('Usage: verify_apk_identity.py AAPT APK EXPECTED_PACKAGE EXPECTED_LABEL')
aapt, apk, expected_package, expected_label = sys.argv[1:]
badging = subprocess.check_output([aapt, 'dump', 'badging', apk], text=True)
package = re.search(r"^package: name='([^']+)'", badging, re.MULTILINE)
assert package and package.group(1) == expected_package, 'Wrong installed application ID'
labels = re.findall(r"^application-label(?:-[^:]+)?:'([^']*)'", badging, re.MULTILINE)
assert labels and all(label == expected_label for label in labels), f'Wrong labels: {labels}'
assert "launchable-activity: name='com.swordfish.lemuroid.app.mobile.feature.main.MainActivity'" in badging
assert 'leanback-launchable-activity:' in badging, 'Missing TV launcher'
print(f'PASS: APK package, all resolved labels, phone and TV launchers: {expected_package}')
