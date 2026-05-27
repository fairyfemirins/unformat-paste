"""
hotkey.py: Platform-specific hotkey registration.
"""
import platform


def register_hotkey(callback):
    """Register Ctrl+V hotkey."""
    system = platform.system()
    if system == "Linux":
        from pynput import keyboard
        def on_activate():
            if keyboard.Controller().ctrl_pressed:
                callback()
        listener = keyboard.GlobalHotKeys({'<ctrl>+v': on_activate})
        listener.start()
    elif system == "Windows":
        import pywin32
        # TODO: Implement Windows hotkey
        pass
    elif system == "Darwin":
        # TODO: Implement macOS hotkey
        pass


def unregister_hotkey():
    """Unregister hotkey."""
    pass