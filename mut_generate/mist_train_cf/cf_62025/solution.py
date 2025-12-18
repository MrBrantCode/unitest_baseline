"""
QUESTION:
Create a function named `validate_string` that takes a string `s` as input and returns `True` if the string matches the following conditions, and `False` otherwise:

- The string starts with a unique non-alphanumeric symbol.
- The non-alphanumeric symbol is followed by exactly three lowercase alphabetic characters.
- The string ends with a minimum of two and a maximum of four numerical digits.
- The string consists only of the specified characters, with no additional characters before, between, or after them.
"""

import re

def validate_string(s):
    pattern = r'^[^a-zA-Z0-9][a-z]{3}\d{2,4}$'
    return bool(re.match(pattern, s))