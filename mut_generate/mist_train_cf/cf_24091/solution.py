"""
QUESTION:
Create a function `validate_email` that checks if a given string represents a valid email address. The email should consist of three parts: a username, a domain, and a top-level domain. The username can contain letters (both uppercase and lowercase), numbers, and the special characters dot (.), hyphen (-), underscore (_), and plus sign (+). The domain can contain letters, numbers, and hyphens. The top-level domain should be at least two characters long and can contain letters, numbers, dots, and hyphens.
"""

import re

def validate_email(email):
    """
    Checks if a given string represents a valid email address.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$"
    return bool(re.match(pattern, email))