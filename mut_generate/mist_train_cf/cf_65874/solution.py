"""
QUESTION:
Create a function named `normalize` that takes a string as input and returns its Unicode NFC normalization form in lowercase. The function should be able to handle higher-level Unicode characters.
"""

import unicodedata

def normalize(s):
    normalized_str = unicodedata.normalize('NFC', s)
    return normalized_str.lower()