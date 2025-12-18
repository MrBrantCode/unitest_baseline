"""
QUESTION:
Create a Python function named `remove_unicode_chars` that takes a string as input and returns the string with all non-ASCII (Unicode) characters removed. The function should utilize regular expressions to replace the Unicode characters. Note that this function will also remove non-ASCII text.
"""

import re

def remove_unicode_chars(string):
    # replace non-ASCII (Unicode) characters with ''
    new_string = re.sub(r'[^\x00-\x7F]+','', string)
    return new_string