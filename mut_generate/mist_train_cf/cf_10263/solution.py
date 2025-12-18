"""
QUESTION:
Create a function `remove_punctuation` that takes a string as input and returns a copy of the string with all punctuation marks removed. Punctuation marks include any characters that are not letters, numbers, or whitespace characters. The function should handle empty strings, strings containing only punctuation marks, special characters, and non-ASCII characters.
"""

import re

def remove_punctuation(s):
    pattern = r'[^\w\s]'
    return re.sub(pattern, '', s)