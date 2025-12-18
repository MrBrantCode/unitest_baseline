"""
QUESTION:
Write a function `clear_line_breaks` that takes a string as input and returns the string with all line breaks replaced with a space and leading/trailing white spaces removed from each line.
"""

import re

def clear_line_breaks(string):
    string = string.replace('\n', ' ')
    string = re.sub(r'^\s+|\s+$', '', string, flags=re.MULTILINE)
    return string