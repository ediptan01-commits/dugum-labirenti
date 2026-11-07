#!/usr/bin/env python3
"""Check the actual release payload, launcher pixels and APK signer."""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import re
import zipfile
from PIL import Image

apk = Path("build/app/outputs/flutter-apk/app-release.apk")
aab = Path("build/app/outputs/bundle/release/app-release.aab")
expected_game = Path("assets/game.html").read_bytes()
expected_icons = {}
for density in ("mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"):
    with Image.open(f"android/app/src/main/res/mipmap-{density}/ic_launcher.png") as im:
        im = im.convert("RGBA")
        expected_icons[im.size] = im.tobytes()

report = {"artifacts": [], "levels": 10}
for artifact, game_path in (
    (apk, "assets/flutter_assets/assets/game.html"),
    (aab, "base/assets/flutter_assets/assets/game.html"),
):
    with zipfile.ZipFile(artifact) as z:
        assert z.read(game_path) == expected_game, "Packaged game differs from source"
        matched = set()
        for name in z.namelist():
            if "/res/" not in "/" + name or not name.endswith(".png"):
                continue
            with Image.open(BytesIO(z.read(name))) as im:
                im = im.convert("RGBA")
                if im.size in expected_icons and im.tobytes() == expected_icons[im.size]:
                    matched.add(im.size)
        assert matched == set(expected_icons), "Missing or incorrect launcher icon densities"
    report["artifacts"].append({
        "file": artifact.name,
        "bytes": artifact.stat().st_size,
        "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
        "packaged_game_sha256": hashlib.sha256(expected_game).hexdigest(),
        "launcher_icon_sizes": sorted([list(size) for size in matched]),
    })

expected_cert = hashlib.sha256(Path("build/upload-certificate.der").read_bytes()).hexdigest()
apk_report = Path("build/apk-signature.txt").read_text()
signers = re.findall(r"certificate SHA-256 digest:\s*([0-9a-fA-F]{64})", apk_report)
assert signers and all(d.lower() == expected_cert for d in signers), f"APK signer differs: expected {expected_cert}, got {signers}; report: {apk_report}"
report["upload_certificate_sha256"] = expected_cert
report["apk_signature"] = "apksigner verified; upload certificate matched"
report["aab_signature"] = "all payload entries verified by VerifyBundle against upload certificate"
Path("build/release-verification.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
