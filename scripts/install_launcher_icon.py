#!/usr/bin/env python3
"""Create Android launcher mipmaps from the project's scalable game-board icon."""
from pathlib import Path
import cairosvg
from PIL import Image
from io import BytesIO

source = Path("assets/launcher_icon.svg").read_bytes()
sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
root = Path("android/app/src/main/res")
for density, size in sizes.items():
    folder = root / f"mipmap-{density}"
    folder.mkdir(parents=True, exist_ok=True)
    png = cairosvg.svg2png(bytestring=source, output_width=size, output_height=size)
    (folder / "ic_launcher.png").write_bytes(png)
    print(f"Launcher icon generated: {density}, {size} x {size}")
store = Path("assets/store_icon_512.png")
store.write_bytes(cairosvg.svg2png(bytestring=source, output_width=512, output_height=512))
print("Store icon generated: " + str(store))
