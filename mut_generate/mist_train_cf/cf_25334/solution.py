"""
QUESTION:
Create a function named `validate_email` that takes a string as an input representing an email address. Using a regular expression, determine if the provided email address is valid or not. The function should return `True` for valid email addresses and `False` otherwise. The email address is valid if it contains one `@` symbol and at least one `.` symbol after the `@` symbol, and no whitespace characters.
"""

import re

def validate_email(email):
    """
    Validate an email address using a regular expression.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    email_pattern = re.compile(r'\S+@\S+\.\S+')
    return bool(re.match(email_pattern, email))