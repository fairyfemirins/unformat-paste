"""
clipboard.py: Platform-agnostic clipboard logic.
"""
import re


def strip_formatting(text: str) -> str:
    """Remove HTML/RTF formatting from text."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove RTF control words and braces
    text = re.sub(r'\\\w+', '', text)
    text = re.sub(r'[{}]', '', text)
    # Collapse whitespace
    text = ' '.join(text.split())
    return text