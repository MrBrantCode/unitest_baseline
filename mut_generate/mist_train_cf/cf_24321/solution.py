"""
QUESTION:
Write a function `validate_email` that takes a string as input and returns `True` if the string is a valid email address and `False` otherwise. A valid email address should contain the "@" symbol, have a domain name after the "@", and end with a top-level domain (2-3 characters) preceded by a dot. The function should use regular expressions to match the input string.
"""

import re

def validate_email(email):
    """
    Validate if a given string is a valid email address.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    pattern = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    return bool(re.match(pattern, email))