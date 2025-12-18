"""
QUESTION:
Write a function `removeSpecialCharacters` that takes a string as input and returns the modified string after removing all punctuation and special characters except hyphens and underscores. The function should be case-insensitive, replace spaces with hyphens, and remove any consecutive hyphens or underscores.
"""

import re

def removeSpecialCharacters(s):
    s = re.sub(r'[^\w\s_-]', '', s)
    s = re.sub(r'\s+', '-', s)
    s = re.sub(r'-+', '-', s)
    s = re.sub(r'_+', '_', s)
    return s.lower()