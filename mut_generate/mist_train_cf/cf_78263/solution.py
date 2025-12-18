"""
QUESTION:
Create a function `is_hex_and_vowel_match` that takes a string as input and returns True if the string consists of one or more hexadecimal digits (0-9, A-F, a-f) immediately followed by a lowercase vowel (a, e, i, o, u), and False otherwise.
"""

import re

def is_hex_and_vowel_match(string):
    pattern = re.compile(r'[0-9A-Fa-f]+[aeiou]')
    return bool(pattern.fullmatch(string))