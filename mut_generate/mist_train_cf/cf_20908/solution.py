"""
QUESTION:
Create a regular expression that captures all words in a given text that start with a vowel (a, e, i, o, u) and end with a digit. The regular expression should match whole words only, not parts of words.
"""

import re

def entrance(text):
    """
    Capture all words in a given text that start with a vowel and end with a digit.

    Args:
        text (str): The input text to search for words.

    Returns:
        list: A list of words that start with a vowel and end with a digit.
    """
    pattern = r'\b[aeiou]\w*\d\b'
    return re.findall(pattern, text, flags=re.IGNORECASE)