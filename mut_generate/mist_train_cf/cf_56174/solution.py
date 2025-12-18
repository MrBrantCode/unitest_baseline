"""
QUESTION:
Create a function called `detect_sequences` that takes a string as input and returns `True` if the string starts with an uppercase 'M' and ends with a lowercase 'x', and `False` otherwise. The function should be able to match any characters (including none) between the 'M' and 'x'. Assume the input string represents a single sequence.
"""

import re

def detect_sequences(string):
    pattern = r'^M.*x$'
    return bool(re.match(pattern, string))