"""
QUESTION:
Write a function `match_string_pattern(string1, string2)` that takes two strings as input and checks if they match the regular expression `/^[a-z]+$/` using the `re` module. The function should return a string stating whether both strings, only one of them, or neither match the pattern.
"""

import re

def match_string_pattern(string1, string2):
    pattern = re.compile(r'^[a-z]+$')

    match_string1 = bool(pattern.match(string1))
    match_string2 = bool(pattern.match(string2))

    if match_string1 and match_string2:
        return "Both strings match the pattern"
    elif match_string1:
        return "Only String1 matches the pattern"
    elif match_string2:
        return "Only String2 matches the pattern"
    else:
        return "Neither strings match the pattern"