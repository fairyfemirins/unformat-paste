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
MIT## Note
This repository is published under `fairyfemirins` due to GitHub namespace restrictions. A transfer to `femirins` is pending.

To request a transfer:
1. Open an issue in this repository.
2. Contact `@femirins` on GitHub.

## Manual Transfer Process
1. Navigate to: [https://github.com/fairyfemirins/unformat-paste/settings](https://github.com/fairyfemirins/unformat-paste/settings)
2. Under "Danger Zone", select "Transfer ownership".
3. Enter the target namespace (`femirins`) and confirm.

## Setup
```bash
git clone https://github.com/fairyfemirins/unformat-paste.git
cd unformat-paste
```