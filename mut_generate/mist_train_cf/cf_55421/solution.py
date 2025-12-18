"""
QUESTION:
Write a function `correct_spaces(text)` that takes a string `text` as input and returns the string with all occurrences of multiple consecutive whitespace characters (including spaces and tabs) replaced by a single space. The function should also remove any leading and trailing whitespace.
"""

import re

def correct_spaces(text):
    text = re.sub('\s+', ' ', text)  # Replace multiple spaces and/or tabs with a single space
    return text.strip()  # Remove leading and trailing spaces 