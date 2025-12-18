"""
QUESTION:
Write a function `match_word` that takes a string as input and returns `True` if the string matches the following conditions and `False` otherwise:
- The string starts with a consonant (any letter other than 'a', 'e', 'i', 'o', 'u', or their uppercase equivalents).
- The string contains a single 'a' or 'A' character.
- The string contains at least one digit.
The function should use a regular expression pattern to match the input string.
"""

import re

def match_word(word):
    pattern = re.compile(r'^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\w*[aA]\w*\d\w*$')
    return bool(pattern.match(word))