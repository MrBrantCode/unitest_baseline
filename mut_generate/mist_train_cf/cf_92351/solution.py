"""
QUESTION:
Implement a function `match_strings` that takes two strings as input, `string1` and `string2`, where `string2` can contain any valid regular expression syntax. The function should return `True` if the pattern in `string2` matches `string1`, and `False` otherwise. The function should replace any '*' in `string2` with '.*' to match any characters.
"""

import re

def match_strings(string1, string2):
    pattern = re.escape(string2).replace('\\*', '.*')
    return bool(re.match(pattern, string1))