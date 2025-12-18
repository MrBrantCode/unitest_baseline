"""
QUESTION:
Write a function named `check_email` that takes an email address as input and returns True if the email address meets the following conditions and False otherwise: 
- The email address contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
- The email address does not exceed 50 characters in length.
"""

import re

def check_email(email):
    if len(email) > 50:
        return False
    
    if not re.search("[A-Z]", email):
        return False
    
    if not re.search("[a-z]", email):
        return False
    
    if not re.search("[0-9]", email):
        return False
    
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", email):
        return False
    
    return True