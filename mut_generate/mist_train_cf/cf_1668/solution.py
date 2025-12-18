"""
QUESTION:
Implement a function `validate_email(email)` that returns `True` if the input is a valid email address, following these rules:
- The local part must be between 1 and 64 characters long and can contain alphanumeric characters, dot (.), underscore (_), or hyphen (-).
- The domain part must be between 1 and 255 characters long and can contain alphanumeric characters, dot (.), or hyphen (-).
- The domain must have at least one dot (.) after the @ symbol.
- The email address cannot contain consecutive dots (.) or consecutive hyphens (-).
- The domain and local part cannot start or end with a dot (.) or hyphen (-).
- The domain and local part cannot contain dots (.) or hyphens (-) before or after the underscore (_) character.
- The domain part cannot have consecutive dots (.) or consecutive hyphens (-) after the last dot (.) in the domain.
"""

import re

def validate_email(email):
    """
    Validate an email address.

    Returns:
        bool: True if the input is a valid email address, False otherwise.
    """
    pattern = r'^([a-zA-Z0-9]+[-._])*[a-zA-Z0-9]+@([a-zA-Z0-9]+[-._])*[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))