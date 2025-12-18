"""
QUESTION:
Create a function `validate_password` that takes a string as input and returns True if the string is a valid password and False otherwise. A valid password must contain at least 8 characters, at least one uppercase letter, at least one lowercase letter, and at least one special character.
"""

import re

def validate_password(password):
    """
    Validate a password.

    A valid password must contain at least 8 characters, at least one uppercase letter,
    at least one lowercase letter, and at least one special character.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$"
    return bool(re.match(pattern, password))