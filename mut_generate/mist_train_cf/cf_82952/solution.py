"""
QUESTION:
Extract all positive integers from a given string using the function `extract_positive_integers(s)`. The function should only return integers greater than zero and not match zero or negative numbers. The input string `s` may contain words and special characters in addition to integers.
"""

import re

def extract_positive_integers(s):
    pattern = r'\b[1-9][0-9]*\b' 
    return list(map(int, re.findall(pattern, s)))