"""
QUESTION:
Create a function named `validate_name` that takes a string as input and returns `True` if the string is a valid name and `False` otherwise. A valid name consists only of alphabetic characters (both upper and lower case) and spaces, with no special characters or numbers.
"""

import re

def validate_name(name):
    pattern = "^[A-Za-z ]+$"  # Pattern to match alphabetic characters (upper or lower case) and spaces only
    return bool(re.match(pattern, name))