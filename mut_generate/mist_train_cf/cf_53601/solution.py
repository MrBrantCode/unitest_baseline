"""
QUESTION:
Write a regular expression to match a valid email address. The email address should start with one or more alphanumeric characters, dots, underscores, percent signs, plus or hyphen, followed by @ symbol, then one or more alphanumeric characters, dots or hyphens, and end with a dot and two or more alphabetic characters.
"""

import re

def validate_email(email):
    """
    Validate an email address using regex.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))