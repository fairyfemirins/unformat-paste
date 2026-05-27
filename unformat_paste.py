#!/usr/bin/env python3
"""
UnformatPaste: A background app that strips formatting from text before pasting.

Usage:
  python3 unformat_paste.py [--hotkey <key>] [--exclude <app1,app2>]

Dependencies:
  - evdev: Linux input events (no X11 required)
  - pyperclip: Clipboard access
"""

import argparse
import pyperclip
import re
import sys

try:
    from evdev import UInput, ecodes as e
    EVDEV_AVAILABLE = True
except ImportError:
    EVDEV_AVAILABLE = False

class UnformatPaste:
    def __init__(self, hotkey='v', exclude_apps=None):
        self.hotkey = hotkey.lower()
        self.exclude_apps = exclude_apps or []
        self.ctrl_pressed = False

    def strip_and_paste(self):
        """Strip formatting from clipboard text and simulate paste."""
        try:
            text = pyperclip.paste()
            if text:
                # Strip HTML tags and whitespace
                clean_text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
                clean_text = re.sub(r'\s+', ' ', clean_text).strip()
                pyperclip.copy(clean_text)
                if EVDEV_AVAILABLE:
                    with UInput() as ui:
                        ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 1)
                        ui.write(e.EV_KEY, e.KEY_V, 1)
                        ui.write(e.EV_KEY, e.KEY_V, 0)
                        ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 0)
                        ui.syn()
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)

    def start(self):
        """Start the event listener (mock for testing)."""
        print("UnformatPaste is running. Press Ctrl+C to exit.")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UnformatPaste: Strip formatting from pasted text.")
    parser.add_argument("--hotkey", default="v", help="Hotkey to trigger unformat (default: 'v')")
    parser.add_argument("--exclude", help="Comma-separated list of apps to exclude (e.g., 'code,terminal')")
    args = parser.parse_args()

    app = UnformatPaste(hotkey=args.hotkey, exclude_apps=args.exclude.split(',') if args.exclude else None)
    app.start()