"""
QUESTION:
Create a function `alphanumeric_frequency(s)` that takes a string `s` as input and returns a dictionary where the keys are the unique alphanumeric characters in the string (case-insensitive) and the values are their frequencies. The function should ignore special characters and spaces.
"""

import re
from collections import Counter

def alphanumeric_frequency(s):
    alnum_chars = re.findall(r'\w', s.lower())
    character_freq = Counter(alnum_chars)
    return dict(character_freq)