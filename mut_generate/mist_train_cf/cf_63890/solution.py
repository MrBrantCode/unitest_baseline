"""
QUESTION:
Write a function named `validate_email` that takes a string as input and returns `True` if the string is a valid email address and `False` otherwise. A valid email address is defined as a string that contains at least one period, one '@' symbol, and only alphanumeric characters, underscores, periods, and hyphens.
"""

import re

def validate_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.fullmatch(email_regex, email))