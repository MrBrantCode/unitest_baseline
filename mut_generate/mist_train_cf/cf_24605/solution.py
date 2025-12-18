"""
QUESTION:
Create a function `email_match` that takes a string as input and returns True if the string matches a specific format of email address, False otherwise. The email address should contain a username and a domain, separated by '@'. The username can contain letters (both uppercase and lowercase), numbers, underscores, periods, and hyphens. The domain should contain letters (both uppercase and lowercase), numbers, underscores, periods, and hyphens, followed by a top-level domain extension of 2-5 letters. The email address should not contain any leading or trailing whitespace.
"""

import re

def email_match(email):
    """
    This function checks if the input string matches a specific format of email address.
    
    Parameters:
    email (str): The input string to be checked.
    
    Returns:
    bool: True if the string matches the email format, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}$'
    return bool(re.match(pattern, email))