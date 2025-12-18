"""
QUESTION:
Create a function named `is_valid_email(email)` that takes an email address as input and returns `True` if it is a valid email address and `False` otherwise. The email address is considered valid if it matches the standard email format and the function should utilize Python's `re` module for this purpose. The function should not take any other parameters apart from the email address.
"""

import re

def is_valid_email(email):
    """
    Returns True if the given email is a valid email address, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None