"""
QUESTION:
Write a function `validate_email` to create a basic regex expression that detects a valid email address. The email address should consist of alphanumeric characters, periods, underscores, plus signs, and hyphens, followed by the '@' symbol, then alphanumeric characters and hyphens, a period, and finally alphanumeric characters, periods, and hyphens. The regex expression should match the entire string.
"""

import re

def validate_email(email):
    """
    This function validates an email address using a regular expression.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))