"""
QUESTION:
Write a function `validate_password` that uses a regular expression to check if a given password contains at least one lowercase letter followed by one or more uppercase letters.
"""

import re

def validate_password(password):
    """
    Validate a password if it contains at least one lowercase letter followed by one or more uppercase letters.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    pattern = r"[a-z]+[A-Z]+"
    return bool(re.search(pattern, password))