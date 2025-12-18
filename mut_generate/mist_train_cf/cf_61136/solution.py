"""
QUESTION:
Create a function `validate_password` that takes a password as input and returns `True` if it is valid and `False` otherwise. The password is valid if it contains at least one uppercase alphabet, one lowercase alphabet, one digit, and one special character from the set `[@_!#$%^&*()<>?/\|}{~:]`. The password should not contain any spaces.
"""

import re

def validate_password(password):
    # check for uppercase letter
    if not re.search("[A-Z]", password):
        return False
    # check for lowercase letter
    if not re.search("[a-z]", password):
        return False
    # check for digits
    if not re.search("[0-9]", password):
        return False
    # check for special characters
    if not re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
        return False
    # check for spaces
    if " " in password:
        return False
    return True