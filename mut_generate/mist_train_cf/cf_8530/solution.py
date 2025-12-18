"""
QUESTION:
Implement a function named `validate_email` that takes an email address as input and returns True if the email address is valid, False otherwise. A valid email address must contain an '@' symbol and a domain name.
"""

def validate_email(email):
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    return '@' in email