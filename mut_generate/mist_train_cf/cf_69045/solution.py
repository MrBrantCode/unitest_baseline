"""
QUESTION:
Write a function that splits a given string at underscore (_) characters. The function should use Python's regular expression module (re) and return a list of substrings. The input string should be treated as a raw string where backslashes are literal characters.
"""

import re

def split_string_at_underscore(i):
    return re.split(r'_', i)