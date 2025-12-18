"""
QUESTION:
Create a function `check_password(password)` that checks the validity of a given password based on the following rules: 
- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter.
- The password must contain at least one lowercase letter.
- The password must contain at least one digit.
- The password must contain at least one of the special characters: _, @, or $.
The function should return `True` if the password is valid and `False` otherwise.
"""

import re

def check_password(password):
    """
    Function to check if a password meets defined criteria
    """
    # checking for minimum length
    if len(password) < 8:
        return False

    # checking for uppercase letter
    if not re.search("[A-Z]", password):
        return False

    # checking for lowercase letter
    if not re.search("[a-z]", password):
        return False

    # checking for numericals
    if not re.search("[0-9]", password):
        return False

    # checking for special characters
    if not re.search("[_@$]", password):
        return False

    # if password passed all checks return True
    return True