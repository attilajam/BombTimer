from pathlib import Path

def test_app():
    root = Path(__file__).parent
    main_py = (root / "main.py").read_text()
    assert "Bomb Pomodoro TImer" in main_py, "main.py title missing"
    
    bomb_html = (root / "Bomb.html").read_text()
    assert "Bomb Pomodoro TImer" in bomb_html, "Bomb.html title missing"

    app_path = root / "dist" / "Bomb Pomodoro TImer.app"
    assert app_path.exists(), "App bundle missing"

    print("All checks passed successfully!")

if __name__ == "__main__":
    test_app()
