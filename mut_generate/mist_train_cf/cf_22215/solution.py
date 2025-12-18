"""
QUESTION:
Implement a function `remove_string(s, t)` that removes all occurrences of string `t` from string `s`. The removal should be case-insensitive and the matching should be based on regular expressions.
"""

import re

def remove_string(s, t):
    pattern = re.compile(t, re.IGNORECASE)
    result = re.sub(pattern, '', s)
    return result