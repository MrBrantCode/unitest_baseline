"""
QUESTION:
Write a function named `validate_email` that takes a string as input and returns True if the string is a valid email address with at least one uppercase letter, one lowercase letter, one number, and one special character, and False otherwise. The string must also contain a combination of these characters with a minimum length of 8.
"""

import re

def validate_email(email):
    """
    Validate an email address.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    return bool(re.match(pattern, email))