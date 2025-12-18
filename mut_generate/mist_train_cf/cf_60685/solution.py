"""
QUESTION:
Compose a regular expression function `validate_email` that validates a basic email address, allowing alphanumeric characters and certain special characters, and adhering to the format `localpart@domain`. The domain should contain at least two alphabetical characters. Note: This function should not be used to validate all possible valid email formats according to the RFC 822 standard.
"""

import re

def validate_email(email):
    """
    Validates a basic email address.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))