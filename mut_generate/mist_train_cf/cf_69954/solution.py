"""
QUESTION:
Create a function called `validate_name` that takes a string as input and returns a boolean indicating whether the string is a valid name. The string is considered a valid name if it only contains lowercase alphabetic characters and whitespace, with multiple words separated by a single space.
"""

import re

def validate_name(name):
    pattern = r'^[a-z]+( [a-z]+)*$'
    if re.match(pattern, name):
        return True
    else:
        return False