"""
QUESTION:
Write a function `remove_special_characters` that takes a string as input and returns a new string with all non-alphanumeric characters removed, excluding the restriction that the function should handle the underscore as a non-alphanumeric character.
"""

import re

def remove_special_characters(string):
    pattern = re.compile('[\W_]+')
    return pattern.sub('', string)