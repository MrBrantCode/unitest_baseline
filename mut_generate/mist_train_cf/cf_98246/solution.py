"""
QUESTION:
Write a function `extract_after_first_comma` that takes a string as input and returns all characters following the first comma. The function should use regular expression.
"""

import re

def extract_after_first_comma(s):
    return re.search(r"(?<=,)[^,]*", s)