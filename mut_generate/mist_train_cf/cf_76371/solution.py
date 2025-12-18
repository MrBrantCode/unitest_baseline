"""
QUESTION:
Create a function called `validate_email` that takes a string as input and returns `True` if the string is a valid email address and `False` otherwise. The email address should follow the standard format, which includes alphanumeric characters, ".", "_", "+", and "-" before the "@" symbol, followed by alphanumeric characters, a period, and alphanumeric characters.
"""

import re

def validate_email(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.search(pattern, email):
        return True
    return False