"""
QUESTION:
Create a function `validate_string` that checks if a given string meets the following conditions:
- Starts with a letter
- Contains only letters and numbers
- Is at least 8 characters in length
- Does not contain any repeated characters.
"""

import re

def validate_string(s):
    pattern = r'^(?=.*(\w)\w*\1)\w{7,}$'
    return not bool(re.match(pattern, s))