"""
QUESTION:
Create a function called `replace_special_characters` that takes a string as input and returns a new string where all non-alphanumeric characters are replaced with underscores, preserving the original string length and structure.
"""

import re

def replace_special_characters(text):
    # the '\W' pattern matches any non-alphanumeric character
    return re.sub('\W', '_', text)