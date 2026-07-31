import subprocess
import sys
from pathlib import Path

def build():
    root = Path(__file__).parent
    
    # Generate icns icon if needed
    icon_icns = root / "icon.icns"
    if not icon_icns.exists():
        icon_png = root / "icons" / "icon.png"
        if icon_png.exists():
            iconset = root / "icon.iconset"
            iconset.mkdir(exist_ok=True)
            sizes = [16, 32, 64, 128, 256, 512]
            for s in sizes:
                subprocess.run(["sips", "-z", str(s), str(s), str(icon_png), "--out", str(iconset / f"icon_{s}x{s}.png")], check=True)
            subprocess.run(["iconutil", "-c", "icns", str(iconset), "-o", str(icon_icns)], check=True)
            import shutil
            shutil.rmtree(iconset, ignore_errors=True)

    cmd = [
        "uv", "run", "--with", "pyinstaller", "pyinstaller",
        "--noconfirm", "--onedir", "--windowed",
        "--name", "Bomb Pomodoro TImer",
        "--add-data", "Bomb.html:.",
        "--add-data", "bomb.png:.",
        "--add-data", "bomb_christmas.png:.",
        "--add-data", "digital_7_mono.ttf:.",
        "--add-data", "explosion2.gif:.",
        "--add-data", "*.wav:."
    ]
    if icon_icns.exists():
        cmd.extend(["--icon", str(icon_icns)])
    cmd.append("main.py")

    subprocess.run(cmd, cwd=root, check=True)
    print("Build complete: dist/Bomb Pomodoro TImer.app")

if __name__ == "__main__":
    build()
