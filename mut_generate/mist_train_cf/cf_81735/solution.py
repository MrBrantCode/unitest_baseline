"""
QUESTION:
Create a function named `replace_multiple_spaces` that takes a string `text` as an input and returns the string with all occurrences of multiple consecutive whitespace characters (including spaces, tabs, and newlines) replaced by a single space. The function should utilize the `re.sub` function from Python's `re` module and handle edge cases where the input string contains different types of whitespace characters.
"""

import re

def replace_multiple_spaces(text):
    return re.sub('[\s]+', ' ', text)