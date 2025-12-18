"""
QUESTION:
Create a function `validatePassword` that takes two strings as input, representing two passwords, and returns a boolean value indicating whether both passwords meet the specified criteria. The passwords are valid if they meet the following conditions:
- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character from the set {!, @, #, $, %, ^, &, *}.
"""

import re

def validatePassword(password1: str, password2: str) -> bool:
    if len(password1) < 8 or len(password2) < 8:
        return False
    
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
    return bool(re.match(pattern, password1) and re.match(pattern, password2))