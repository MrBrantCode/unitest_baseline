"""
QUESTION:
Create a function called `validate_email` that takes a string `email` as input. The function should return `True` if the email address is valid and `False` otherwise, based on the following criteria:
- The email address must be of text type.
- The email address must contain a single "@" symbol.
- The domain part of the email address must contain at least one "." symbol.
"""

import re

def validate_email(email):
    if not isinstance(email, str):
        return False
    if email.count('@') != 1:
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True