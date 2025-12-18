"""
QUESTION:
Write a function `validate_string(s)` that checks if the input string `s` meets the following conditions:

- The string starts with a lowercase letter.
- The string contains only alphanumeric characters and underscores.
- The string differentiates between uppercase and lowercase letters.
- The string has a length of exactly 8 to 12 characters.
- The string contains at least one digit.

Return `True` if the string meets all conditions, and `False` otherwise.
"""

import re

def validate_string(s):
    pattern = '^[a-z](.*\d.*)?.{7,11}$'
    return bool(re.match(pattern, s) and any(c.isdigit() for c in s) and re.match("^[A-Za-z0-9_]*$", s))