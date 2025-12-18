"""
QUESTION:
Write a function `remove_occurrences(s)` that takes a string `s` as input and returns a new string with all occurrences of "abcd" and "efgh" removed in a case-insensitive manner. The removal should preserve the original case of the remaining letters in the resulting string. The function should also maintain the original order of the letters in the resulting string.
"""

import re

def remove_occurrences(s):
    pattern = re.compile(r'abcd|efgh', re.IGNORECASE)
    result = re.sub(pattern, '', s)
    return result