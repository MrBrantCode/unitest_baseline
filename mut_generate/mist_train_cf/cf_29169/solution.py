"""
QUESTION:
Implement the function `validateEmail` that takes a string `email` as input and returns a boolean value indicating whether the input string is a valid email address. A valid email address should contain exactly one "@" symbol, with the "@" symbol not being the first or last character. The part before the "@" symbol should have at least one character and only consist of alphanumeric characters, dots, hyphens, and underscores. The part after the "@" symbol should have at least one dot and at least two characters.
"""

import re

def validateEmail(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))