# Unformat Paste
A background CLI tool to paste clipboard content as unformatted text (plaintext) by overloading `Ctrl+V`.

## Problem
When copying text from Office apps (LibreOffice, MS Word) into email clients (Outlook, Thunderbird), formatting (fonts, colors, tables) is preserved. This tool strips formatting automatically.

## Solution
- Runs in the background.
- Intercepts `Ctrl+V` and pastes plaintext.
- Works system-wide (Linux/Windows/macOS).

## Installation
```bash
git clone https://github.com/Femirins/unformat-paste.git
cd unformat-paste
pip install -r requirements.txt
```

## Usage
```bash
python3 unformat_paste.py  # Runs in background. Press Ctrl+C to exit.
```

## Technical Architecture
- **Libraries**: `pyperclip` (clipboard access), `keyboard` (hotkey interception).
- **Workflow**:
  1. User presses `Ctrl+V`.
  2. Tool reads clipboard content.
  3. Tool simulates `keyboard.write()` with plaintext.

## Limitations
- **Linux**: Requires `sudo` (run as `sudo python3 unformat_paste.py`).
- **Wayland**: Not compatible (use X11).
- **macOS/Windows**: No restrictions.

## License
MIT