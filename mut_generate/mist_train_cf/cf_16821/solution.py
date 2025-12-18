"""
QUESTION:
Create a function that uses a regular expression to match any word that starts with the letter "a" and is followed by exactly two digits, with the restriction that the word must not contain any repeating digits.
"""

import re

def entrance(word):
    pattern = r'\b(a(?!\d*(\d)\d*\2)\d{2})\b'
    return bool(re.match(pattern, word))