"""
QUESTION:
Design a function `match_string(s)` that takes a string `s` as input and returns `True` if the string starts with the letter "a", contains at least one digit, and contains at least one uppercase letter, and `False` otherwise. The order of the digit and uppercase letter does not matter, and the matching is case-sensitive.
"""

import re

def match_string(s):
    pattern = r'^a.*([0-9]).*([A-Z])|(^a.*([A-Z]).*([0-9]))'
    if re.search(pattern, s):
        return True
    return False