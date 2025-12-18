"""
QUESTION:
Create a function named `validate_email` that takes an email address as input and returns `True` if it is valid and `False` otherwise. The function should use a regular expression to check if the email conforms to the general email pattern (RFC standards) and common domain extensions like .com, .org, .edu, .net. The solution should prioritize simplicity and readability over full RFC compliance.
"""

import re

def validate_email(email):
    """
    Validate if an email address is in a general email format.
    
    Parameters:
    email (str): The email address to be validated.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(pattern, email) is not None