"""
QUESTION:
Implement a function `validate_password(password: str) -> bool` that takes a password as input and returns `True` if the password meets the following rules, and `False` otherwise:
- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character from the set {!, @, #, $, %, ^, &, *}.
"""

import re

def validate_password(password: str) -> bool:
    # Rule 1: Check minimum length
    if len(password) < 8:
        return False
    
    # Rule 2: Check for required characters using regular expressions
    if not re.search(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])", password):
        return False
    
    return True