#!/usr/bin/env python3
"""
Test script for UnformatPaste.

Usage:
  python3 test_unformat_paste.py
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
sys.path.insert(0, '.')
from unformat_paste import UnformatPaste

class TestUnformatPaste(unittest.TestCase):
    def setUp(self):
        self.app = UnformatPaste(hotkey='v')

    def test_strip_and_paste(self):
        """Test that formatted text is stripped."""
        with patch('pyperclip.paste', return_value="<b>Test</b>  formatted\ntext"), \
             patch('pyperclip.copy') as mock_copy:
            self.app.strip_and_paste()
            mock_copy.assert_called_once_with("Test formatted text")

    def test_strip_and_paste_empty(self):
        """Test that empty clipboard is handled."""
        with patch('pyperclip.paste', return_value=""), \
             patch('pyperclip.copy') as mock_copy:
            self.app.strip_and_paste()
            mock_copy.assert_not_called()

if __name__ == "__main__":
    unittest.main()