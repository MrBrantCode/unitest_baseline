"""
QUESTION:
Write a function `check_email` that takes an email address as input and returns `True` if it meets the following conditions, and `False` otherwise: 
- The email address contains at least one uppercase letter, one lowercase letter, one digit, and one special character. 
- The email address has a maximum length of 50 characters.
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