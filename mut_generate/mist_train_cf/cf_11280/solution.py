"""
QUESTION:
Create a function `validate_string` that checks if a given string meets the following conditions: 
- The string length is between 10 and 30 characters (inclusive).
- The first character is a lowercase letter.
- The last character is an uppercase letter.
- All characters in between can be any alphanumeric character.
"""

import re

def validate_string(s):
    pattern = r"^[a-z][a-zA-Z0-9]{8,28}[A-Z]$"
    return bool(re.match(pattern, s))