"""
QUESTION:
Write a function `validate_email` to validate an email address. The function should use a regular expression to check if the email address is valid, including checking the domain name, top-level domain (TLD), and country code top-level domain (ccTLD). The TLD or ccTLD should be valid and recognized. The function should return True if the email is valid and False otherwise.
"""

import re

def validate_email(email):
    """
    Validate an email address using a regular expression.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    pattern = r"^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2})?$"
    return bool(re.match(pattern, email))