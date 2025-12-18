"""
QUESTION:
Write a function `validate_email` that takes an input string and returns `True` if the string is a valid email address and `False` otherwise. The email address is considered valid if it starts with one or more alphanumeric characters, followed by the "@" symbol, then one or more alphanumeric characters, a dot ("."), and ends with two to four alphabetic characters.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$"
    return bool(re.match(pattern, email))