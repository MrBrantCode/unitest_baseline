"""
QUESTION:
Create a function called `is_valid_email(email)` that takes an email address as input and returns `True` if the email is valid, `False` otherwise. The email address is valid if it meets the following criteria: 
- its length is between 8 and 100 characters (inclusive),
- it contains an "@" symbol,
- its domain name has at least 3 characters,
- it does not contain any special characters other than ".", "-", "_", and "@" in the correct positions,
- its domain name contains at least one dot (.) and the characters after the dot are letters only,
- its local part (the part before the "@" symbol) does not start or end with a special character.
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