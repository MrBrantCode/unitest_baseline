"""
QUESTION:
Create a regular expression that matches a string enclosed in parentheses, containing the digit '1' followed by exactly two '0's.
"""

import re

def entrance(s):
    pattern = r'\(100\)'
    return bool(re.match(pattern, s))