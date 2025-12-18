"""
QUESTION:
Write a function `has_consecutive_special_chars` that takes a string as input and returns `True` if the string contains at least three consecutive special characters, and `False` otherwise. A special character is defined as any character that is not a word character (`\w`) or a whitespace character (`\s`).
"""

import re

def has_consecutive_special_chars(string):
    pattern = r"[^\w\s]{3,}"
    match = re.search(pattern, string)
    if match:
        return True
    return False