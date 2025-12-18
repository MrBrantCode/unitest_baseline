"""
QUESTION:
Create a function called `regex_match` that takes two strings as input: `string1` and `string2`, where `string2` can contain any valid regular expression syntax. The function should return `True` if the pattern in `string2` matches `string1` and `False` otherwise. Note that the `*` character in `string2` should be treated as a wildcard that matches any characters (including none).
"""

import re

def regex_match(string1, string2):
    pattern = re.escape(string2).replace('\\*', '.*')
    return bool(re.match(pattern, string1))