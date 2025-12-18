"""
QUESTION:
Create a function `validate_email` that takes an email address as input and returns `True` if the email is valid, `False` otherwise. A valid email address must contain at least one uppercase letter and one lowercase letter, in addition to following standard email address format rules. The function should use Regular Expressions to validate the email address.
"""

import re

def validate_email(email):
    """
    Validate an email address.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email address is valid, False otherwise.

    A valid email address must contain at least one uppercase letter and one lowercase letter, 
    in addition to following standard email address format rules.
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"
    return bool(re.search(pattern, email))