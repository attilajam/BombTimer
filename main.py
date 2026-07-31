import sys
from pathlib import Path
import webview

class API:
    def resize(self, width, height):
        if webview.windows:
            webview.windows[0].resize(int(width), int(height))

def main():
    api = API()
    # ponytail: naive sys._MEIPASS check; upgrade path is importlib.resources if packaged as a python wheel
    base_dir = Path(sys._MEIPASS) if getattr(sys, "frozen", False) else Path(__file__).parent
    html_path = base_dir / "Bomb.html"
    width, height = 260, 280
    screen = webview.screens[0] if webview.screens else None
    x = screen.x + screen.width - width + 10 if screen else None
    webview.create_window(
        "Bomb Pomodoro TImer",
        str(html_path),
        width=width,
        height=height,
        x=x,
        y=0 if screen else None,
        screen=screen,
        frameless=True,
        transparent=True,
        on_top=True,
        resizable=True,
        min_size=(width, height),
        easy_drag=False,
        js_api=api,
    )
    webview.start()

if __name__ == "__main__":
    main()
