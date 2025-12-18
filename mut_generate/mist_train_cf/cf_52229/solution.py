"""
QUESTION:
Create a function `validate_string(s)` that validates a given string according to the following rules: 
- The string should start with a non-alphanumeric character.
- The string should be followed by exactly three lowercase alphabetic characters.
- The string should end with a numeric sequence of 2 to 4 digits inclusively.
"""

import re

def entrance(s):
    pattern = r'^\W[a-z]{3}\d{2,4}$'
    if re.match(pattern, s):
        return True
    return False