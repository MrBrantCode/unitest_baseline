"""
QUESTION:
Write a function `is_valid_email(email)` that takes a string `email` as input and returns `True` if the string represents a valid email address and `False` otherwise. The function should validate the structure of the email address, including valid characters, symbol placement, and domain extension, but may not cover all edge cases as specified in the email address specification RFC 5322. The function should allow standard email formats, including subdomains and domain extensions of more than one level.
"""

import re

def is_valid_email(email):
    """
    Validate the structure of an email address.

    Args:
    email (str): Email address to be validated.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.search(pattern, email))