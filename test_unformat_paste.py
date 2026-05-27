"""
test_unformat_paste.py: Unit tests for unformat-paste.
"""
import unittest
from unittest.mock import patch, MagicMock
from clipboard import strip_formatting


class TestUnformatPaste(unittest.TestCase):
    def test_strip_formatting(self):
        # Test HTML stripping
        html_text = "<b>Hello</b> <i>World</i>"
        self.assertEqual(strip_formatting(html_text), "Hello World")
        
        # Test RTF stripping
        rtf_text = r"{\rtf1\b Hello} {\i World}"
        self.assertEqual(strip_formatting(rtf_text), "Hello World")
        
        # Test whitespace collapse
        spaced_text = "Hello\n\t  World"
        self.assertEqual(strip_formatting(spaced_text), "Hello World")


if __name__ == "__main__":
    unittest.main()