"""
QUESTION:
Create a function called `remove_special_characters` that takes a string as input and returns the string with all special characters removed, except for the '@' symbol.
"""

import re

def remove_special_characters(string):
    pattern = r'[^a-zA-Z0-9@ ]+'
    return re.sub(pattern, '', string)