"""
QUESTION:
Write a regular expression function to validate email addresses. The function should accept strings as input, match one or more of the allowed characters (a-z, A-Z, 0-9, _, +, -) before the '@' symbol, match one or more of the allowed characters (a-z, A-Z, 0-9, '-') for the domain name before the dot, and match one or more of the allowed characters (a-z, A-Z, 0-9, '.') for the TLD or ccTLD. The function should also ensure there are no consecutive dots in the email address.
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
    pattern = r"^(?!.*\.\.)[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))