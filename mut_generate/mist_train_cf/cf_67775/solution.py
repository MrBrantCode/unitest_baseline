"""
QUESTION:
Create a function called `consonant_pattern_matcher` that checks if a given string consists solely of consonants and follows a user-defined pattern of consonants. The function should take two parameters: the input string `s` and the pattern `pattern`. The function should return `True` if the string meets both conditions and `False` otherwise. The pattern should be treated as a regular expression, and the function should be efficient enough to handle large input strings.
"""

import re

def consonant_pattern_matcher(s, pattern):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for char in s:
        if char not in consonants:
            return False
    compiled_pattern = re.compile(pattern)
    return compiled_pattern.fullmatch(s) is not None