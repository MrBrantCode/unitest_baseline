"""
QUESTION:
Create a function `check_compatibility` that takes two string parameters `string1` and `string2` and returns a boolean value indicating whether both strings match the regular expression `^[a-z]+$`. The function should return `True` if both strings contain only lowercase letters from 'a' to 'z' with one or more occurrences, and `False` otherwise.
"""

import re

def check_compatibility(string1, string2):
    pattern = "^[a-z]+$"
    return bool(re.match(pattern, string1)) and bool(re.match(pattern, string2))