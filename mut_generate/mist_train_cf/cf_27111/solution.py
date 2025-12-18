"""
QUESTION:
Create a function `validatePassword` that takes two string parameters, `password` and `confirmPassword`, and returns a boolean value. The function should return `true` if `password` and `confirmPassword` match, `password` is at least 8 characters long, and contains at least one uppercase letter, one lowercase letter, one digit, and one special character (such as !, @, #, $, %, ^, &, *). Otherwise, the function should return `false`.
"""

import re

def validatePassword(password, confirmPassword):
    # Check if passwords match
    if password != confirmPassword:
        return False
    
    # Check password strength criteria
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*]", password):
        return False
    
    return True