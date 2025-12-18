"""
QUESTION:
Implement a function `validatePassword` that takes a string representing a password as input. The password is valid if it meets the following criteria: 
- The password length is at least 8 characters.
- The password contains at least one uppercase letter, one lowercase letter, one digit, and one special character from the set {!, @, #, $, %, ^, &, *}.
The function should return `True` if the password is valid and `False` otherwise.
"""

import re

def validatePassword(password):
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password) or not re.search(r"[!@#$%^&*]", password):
        return False
    
    return True