"""
QUESTION:
Create a regular expression to validate an e-mail address. The function should match most common email address formats.
"""

import re

def validate_email(email):
    """
    Validate an email address using a regular expression.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    return bool(re.match(pattern, email))