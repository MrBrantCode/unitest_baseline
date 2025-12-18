"""
QUESTION:
Write a function `is_valid_email` that takes a string as input and returns `True` if the string is a valid email address and `False` otherwise. A valid email address should contain the `@` symbol separating the local part from the domain, the local part can contain alphanumeric characters, dots, and hyphens, and the domain should have at least two characters and at most four characters after the top-level domain. The function should use a regular expression to validate the email address.
"""

import re

def is_valid_email(email):
    """
    This function checks if a given string is a valid email address.
    
    Args:
        email (str): The input string to be validated.
    
    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,4}$"
    return bool(re.match(pattern, email))