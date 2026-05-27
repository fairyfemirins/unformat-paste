# UnformatPaste

**UnformatPaste** is a lightweight background app that strips formatting from text before pasting. It hooks `Ctrl+V` globally and replaces the clipboard content with plain text.

## Features
- **Cross-Platform**: Works on Linux (headless/desktop).
- **Minimal Dependencies**: Only `evdev` and `pyperclip`.
- **Configurable**: Set custom hotkeys or exclude apps.

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install evdev pyperclip
```

## Usage
```bash
# Start the app (default hotkey: Ctrl+V)
python3 unformat_paste.py

# Custom hotkey (e.g., Ctrl+Shift+V)
python3 unformat_paste.py --hotkey V
```

## Testing
```bash
python3 -m pytest test_unformat_paste.py -v
```

## License
MIT