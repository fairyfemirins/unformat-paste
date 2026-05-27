# unformat-paste

**Unformat text before pasting — system-wide, cross-platform.**

## Problem
Copying formatted text (e.g., from Office apps) into plaintext editors (e.g., Notepad, terminals) retains unwanted formatting (bold, italics, colors). Users must manually paste into Notepad first to strip formatting.

## Solution
`unformat-paste` is a CLI tool that:
- Monitors the clipboard for changes.
- Strips HTML/RTF formatting on `Ctrl+V`.
- Works system-wide (Windows/macOS/Linux).

## Usage
```bash
# Run as daemon
unformat-paste start

# One-time paste
unformat-paste once

# Stop daemon
unformat-paste stop
```

## Technical Architecture
- **Clipboard:** `pyperclip` (cross-platform clipboard access).
- **Hotkeys:** Platform-specific hooks (`pynput` for Linux, `pywin32` for Windows).
- **Formatting:** Regex-based HTML/RTF stripping.

## Limitations
- **Linux:** Requires `xclip` (`sudo apt-get install xclip`).
- **Windows/macOS:** Hotkey registration not yet implemented (contributions welcome!).

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

## Repository URL
[https://github.com/fairyfemirins/unformat-paste](https://github.com/fairyfemirins/unformat-paste)