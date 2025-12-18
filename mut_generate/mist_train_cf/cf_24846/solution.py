"""
QUESTION:
Create a function `match_string` that returns True if a given string starts with a lowercase 'a' and ends with an uppercase 'Z', and False otherwise.
"""

import re

def match_string(s):
    return bool(re.match(r'^a.*Z$', s))