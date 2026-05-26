#!/usr/bin/env python3
import pyperclip
import keyboard
import time
import sys

def paste_unformatted():
    """Paste clipboard content as unformatted text."""
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            # Simulate Ctrl+Shift+V (unformatted paste)
            keyboard.write(clipboard_content)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

def main():
    print("Unformat Paste: Running in background. Press Ctrl+C to exit.")
    keyboard.add_hotkey('ctrl+v', paste_unformatted)
    keyboard.wait()

if __name__ == "__main__":
    main()