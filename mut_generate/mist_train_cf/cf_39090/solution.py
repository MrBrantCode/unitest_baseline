"""
QUESTION:
Create a function `is_password_strong(password)` that evaluates the strength of a given password based on the following criteria: 
- the password is at least 8 characters long, 
- the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character (!, @, #, $, %, ^, &, *), 
- the password does not contain the word "password" in any case. 

The function should return a boolean value indicating whether the password is strong (True) or weak (False).
"""

import re

def is_password_strong(password):
    if len(password) < 8:
        return False
    if re.search(r'[A-Z]', password) is None:
        return False
    if re.search(r'[a-z]', password) is None:
        return False
    if re.search(r'\d', password) is None:
        return False
    if re.search(r'[!@#$%^&*]', password) is None:
        return False
    if re.search(r'password', password, re.IGNORECASE) is not None:
        return False
    return True