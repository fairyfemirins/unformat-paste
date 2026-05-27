#!/usr/bin/env python3
"""
unformat-paste: A CLI tool to strip formatting from clipboard text before pasting.
Usage:
  unformat-paste start   # Run as daemon
  unformat-paste stop    # Kill daemon
  unformat-paste once    # One-time paste
"""

import sys
import signal
import pyperclip
from hotkey import register_hotkey, unregister_hotkey
from clipboard import strip_formatting

DAEMON_PID = None


def paste_unformatted():
    """Replace clipboard content with plain text."""
    try:
        text = pyperclip.paste()
        plain_text = strip_formatting(text)
        pyperclip.copy(plain_text)
        print("Pasted as plain text!")
    except Exception as e:
        print(f"Error: {e}")


def start_daemon():
    """Start the daemon to monitor clipboard."""
    global DAEMON_PID
    if DAEMON_PID:
        print("Daemon already running!")
        return
    
    pid = os.fork()
    if pid == 0:
        # Child process
        register_hotkey(paste_unformatted)
        signal.pause()  # Wait for hotkey
    else:
        DAEMON_PID = pid
        print(f"Daemon started (PID: {pid})")


def stop_daemon():
    """Stop the daemon."""
    global DAEMON_PID
    if not DAEMON_PID:
        print("No daemon running!")
        return
    
    os.kill(DAEMON_PID, signal.SIGTERM)
    unregister_hotkey()
    DAEMON_PID = None
    print("Daemon stopped")


def main():
    if len(sys.argv) < 2:
        print("Usage: unformat-paste [start|stop|once]")
        return
    
    command = sys.argv[1]
    if command == "start":
        start_daemon()
    elif command == "stop":
        stop_daemon()
    elif command == "once":
        paste_unformatted()
    else:
        print("Invalid command")


if __name__ == "__main__":
    import os
    main()