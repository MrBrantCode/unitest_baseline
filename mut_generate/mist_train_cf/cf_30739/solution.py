"""
QUESTION:
Create a function named `validate_password` that takes a string `password` as input and returns a boolean value indicating whether the password is valid according to the following rules: 
- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character from the set {!, @, #, $, %, ^, &, *}.
"""

import re

def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password) or not re.search(r"[!@#$%^&*]", password):
        return False
    
    return True