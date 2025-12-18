"""
QUESTION:
Create a function called `is_valid_email` that takes a string as input. The function should return `True` if the string is a valid email address and `False` otherwise. A valid email address must have a length between 8 and 100 characters, contain an "@" symbol, and have a domain name with at least 3 characters. The email address must be in a valid format, with no special characters other than ".", "-", "_", and "@" in the correct positions. The domain name must contain at least one dot (.) and the characters after the dot must be letters only. The local part of the email address must not start or end with a special character.
"""

import re

def is_valid_email(email):
    # Check length
    if len(email) < 8 or len(email) > 100:
        return False
    
    # Check "@" symbol and domain name
    if "@" not in email or len(email.split("@")) != 2:
        return False
    
    local_part, domain_part = email.split("@")
    
    # Check local part
    if local_part[0] in ('.', '-', '_') or local_part[-1] in ('.', '-', '_'):
        return False
    
    # Check format
    if not re.match(r'^[\w\-.]+@[\w\-.]+\.[A-Za-z]+$', email):
        return False
    
    # Check domain name
    if "." not in domain_part or not domain_part.split(".")[-1].isalpha():
        return False
    
    return True