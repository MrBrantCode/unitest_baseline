"""
QUESTION:
Create a function `eliminate_spaces(text)` that takes a string as input and returns a new string where all occurrences of multiple spaces (two or more consecutive spaces) are replaced with a single space.
"""

import re

def eliminate_spaces(text):
    # use a regular expression to replace one or more occurrences of spaces with a single space
    condensed_text = re.sub(' +', ' ', text)
    return condensed_text