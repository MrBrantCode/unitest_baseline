"""
QUESTION:
Create a function `validate_email(email)` that takes an email string as input and returns `True` if the email is valid and `False` otherwise. The email is considered valid if it matches the standard email format.
"""

import re

def validate_email(email):
    """
    Validate an email string.
    
    Args:
    email (str): The email to be validated.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return bool(re.search(regex, email))