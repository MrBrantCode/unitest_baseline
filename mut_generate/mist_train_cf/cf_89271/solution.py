"""
QUESTION:
Create a function `validate_email` that takes an email address as input and returns True if the email is valid, False otherwise. A valid email address must match the following conditions:

- Contain at least one uppercase letter and one number in the username part of the email address.
- Exclude any emails that contain the domain "gmail.com" or "yahoo.com".
- Follow the standard format of an email address, including a username, domain name, and top-level domain.

The input is a string representing the email address. The output is a boolean indicating whether the email is valid or not.
"""

import re

def validate_email(email):
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?!.*@(?:gmail\.com|yahoo\.com))\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return bool(re.match(pattern, email))