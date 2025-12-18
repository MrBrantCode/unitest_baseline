"""
QUESTION:
Create a function `find_abcd_pattern` that uses Regular Expression to find words containing the letters "a", "b", "c", and "d" in that specific order and without any additional letters in between.
"""

import re

def find_abcd_pattern(s):
    pattern = r'abcd'
    match = re.search(pattern, s)
    return bool(match)