"""
QUESTION:
Write a function `validate_password` that takes a string `new_password` as input and returns `True` if it meets the following requirements, and `False` otherwise:
- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, and one digit.
- The password must not contain any special characters (i.e., non-alphanumeric characters).
"""

import re

def validate_password(new_password):
    # Check if the password is at least 8 characters long
    if len(new_password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
    if not re.search(r"[A-Z]", new_password) or not re.search(r"[a-z]", new_password) or not re.search(r"\d", new_password):
        return False
    
    # Check if the password does not contain any special characters
    if re.search(r"\W", new_password):
        return False
    
    return True