"""
QUESTION:
Write a function named `validate_email` to match the standard email address format. The email address should start with one or more alphanumeric characters or underscores or hyphens, followed by zero or more occurrences of a dot and one or more alphanumeric characters or underscores or hyphens, then an '@' symbol, one or more alphanumeric characters or hyphens, zero or more occurrences of a dot and one or more alphanumeric characters or hyphens, and finally a dot and the domain extension (it should be alphabetic and have a length of 2 to 4 characters).
"""

import re

def validate_email(email):
    """
    Validate an email address.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    regex = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    return bool(re.match(regex, email, re.IGNORECASE))