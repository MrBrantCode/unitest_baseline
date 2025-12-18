"""
QUESTION:
Create a function `verify_string(s)` that takes a string `s` as input and returns `True` if the string starts with a special character, followed by exactly 3 lowercase letters, and ends with at least 2 but not more than 4 digits, and `False` otherwise.
"""

import re

def verify_string(s):
    regex = r"^[^\w\d]\w{3}\d{2,4}$"
    match = re.fullmatch(regex, s)
    return match is not None  # Returns True if the string matches, False otherwise