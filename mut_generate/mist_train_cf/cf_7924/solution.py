"""
QUESTION:
Write a function `validate_email` that checks if a given email address is valid. The function should return True if the email address is valid and False otherwise.

Restrictions: 
- The function should use regular expressions to validate the email address format.
- The function should not use any external libraries or modules.
"""

import re

def validate_email(email):
    """
    Validate an email address using regular expression.
    
    Parameters:
    email (str): The email address to be validated.
    
    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))