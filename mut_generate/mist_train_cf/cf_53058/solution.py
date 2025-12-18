"""
QUESTION:
Design a function named `match_pattern` that takes a string as input and returns True if the string starts with '1' and ends with '@', with any characters in between, and False otherwise. The function should use regular expressions for pattern matching.
"""

import re

def match_pattern(s):
    pattern = r"^1.*@$"
    if(re.match(pattern, s)):
        return True
    return False