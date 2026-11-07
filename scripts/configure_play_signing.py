#!/usr/bin/env python3
"""Configure Flutter-generated Kotlin Gradle for private Play upload signing."""
from pathlib import Path
import os

gradle = Path("android/app/build.gradle.kts")
if not gradle.exists():
    raise SystemExit("Missing generated android/app/build.gradle.kts")
original = gradle.read_text()
old = "signingConfig = signingConfigs.getByName(\"debug\")"
if old not in original:
    raise SystemExit("Expected Flutter debug signing line not found; review generated Gradle version.")

insertion = '''
    signingConfigs {
        create("playUpload") {
            storeFile = file("../upload-keystore.jks")
            storePassword = System.getenv("PLAY_STORE_PASSWORD")
            keyAlias = System.getenv("PLAY_KEY_ALIAS")
            keyPassword = System.getenv("PLAY_KEY_PASSWORD")
        }
    }

'''
marker = "    buildTypes {"
if marker not in original:
    raise SystemExit("Expected buildTypes block not found; review generated Gradle version.")
modified = original.replace(marker, insertion + marker, 1).replace(old, 'signingConfig = signingConfigs.getByName("playUpload")', 1)
gradle.write_text(modified)
print("Release signing configured using GitHub Actions environment secrets.")
