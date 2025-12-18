"""
QUESTION:
Create a function called `is_valid_email` that checks if a given email address is valid. The email address must have a length between 5 and 50 characters, contain an "@" symbol, and have a domain name with at least 2 characters. The email address should also be in a valid format, allowing only alphanumeric characters, ".", "-", "_", and "@" in the correct positions.
"""

import re

def is_valid_email(email):
    # Check length
    if len(email) < 5 or len(email) > 50:
        return False
    
    # Check for @ symbol
    if "@" not in email:
        return False
    
    # Check for domain name with at least 2 characters
    domain = email.split("@")[1]
    if len(domain) < 2:
        return False
    
    # Check for valid format using regular expression
    if not re.match(r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False
    
    return True