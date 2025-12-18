"""
QUESTION:
Create a function called `match_pattern(text)` that returns `True` if the input string contains exactly three distinct words separated by exactly two spaces, and `False` otherwise.
"""

import re

def match_pattern(text):
    pattern = r"(\b\w+\b)  (\b\w+\b)  (\b\w+\b)" 
    result = re.search(pattern, text)
    return result is not None