"""
QUESTION:
Construct a regular expression for a function named `validate_zip(code)` that takes a string `code` as input and returns a boolean value. The function should validate a 6-digit numeric zip code with the following conditions:
- The first three digits must be divisible by 2.
- The last three digits should not start with 0.
"""

import re

def validate_zip(code):
    if re.search(r"^[02468]{3}[1-9][0-9]{2}$", code):
        return True
    else:
        return False