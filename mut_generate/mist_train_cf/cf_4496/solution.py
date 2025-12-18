"""
QUESTION:
Write a function `remove_occurrences(s)` that takes a string `s` as input and returns a new string where all occurrences of "abcd" and "efgh" are removed in a case-insensitive manner. The resulting string should maintain the same case (uppercase/lowercase) as the original string and preserve the order of the letters.
"""

import re

def remove_occurrences(s):
    pattern = re.compile(r'abcd|efgh', re.IGNORECASE)
    result = re.sub(pattern, '', s)
    return result