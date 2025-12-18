"""
QUESTION:
Create a function named `match_string` that takes a string `s` as input and returns `True` if the string contains an octal digit (0-7) followed by an uppercase consonant (all uppercase English letters excluding A, E, I, O, U), and `False` otherwise.
"""

import re

def match_string(s):
    pattern = "[0-7][BCDFGHJKLMNPQRSTVWXYZ]"
    return bool(re.search(pattern, s))