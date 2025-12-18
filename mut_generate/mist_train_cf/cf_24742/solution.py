"""
QUESTION:
Create a function `validate_email` that takes a string as input and returns a boolean value indicating whether the string is a valid email address. A valid email address consists of alphanumeric characters, underscores, and dots before the '@' symbol, followed by alphanumeric characters, underscores, and dots after the '@' symbol, and ends with a dot and at least one lowercase letter.
"""

import re

def validate_email(email):
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.[a-z]+$"
    return bool(re.match(pattern, email))