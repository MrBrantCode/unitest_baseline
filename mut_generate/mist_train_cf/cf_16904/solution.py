"""
QUESTION:
Create a function named `remove_punctuation` that takes a string as input and returns a copy of the string with all punctuation marks and special characters removed, preserving letters, numbers, whitespace, and non-ASCII characters. The function should handle edge cases such as empty strings or strings containing only punctuation marks.
"""

import re

def remove_punctuation(string):
    pattern = r'[^\w\s]'
    string = re.sub(pattern, '', string)
    return string