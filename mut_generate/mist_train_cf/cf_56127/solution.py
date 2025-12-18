"""
QUESTION:
Create a function `match_pattern(text)` that uses a regular expression to determine if the input string `text` matches a pattern consisting of one or more octal digits (0-7) followed by a single uppercase non-vowel alphabetic character. The function should return `True` if the input string matches the pattern and `False` otherwise. The input string should only contain the octal digits and the uppercase non-vowel character, with no other characters before or after.
"""

import re

def match_pattern(text):
    pattern = r'^[0-7]+[BCDFGHJKLMNPQRSTVWXYZ]$'
    return bool(re.search(pattern, text))