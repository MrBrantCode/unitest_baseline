"""
QUESTION:
Implement a Python function `validate_email` that takes an email address as input and returns `True` if it's valid, `False` otherwise. The email address is valid if it meets the following conditions:
1. The local part (before the @ symbol) is between 1 and 64 characters long and contains only alphanumeric characters, dot (.), underscore (_), or hyphen (-).
2. The domain part (after the @ symbol) is between 1 and 255 characters long and contains only alphanumeric characters, dot (.), or hyphen (-).
3. The domain has at least one dot (.) after the @ symbol.
4. The domain does not start or end with a dot (.) or hyphen (-).
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
    pattern = r"^[a-zA-Z0-9_.-]{1,64}@[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))