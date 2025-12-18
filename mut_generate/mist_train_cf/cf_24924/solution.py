"""
QUESTION:
Write a function named `validatePassword` that checks if a given password is valid. The password is valid if it meets the following conditions: 
- it contains at least one lowercase letter
- it contains at least one uppercase letter
- it contains at least one number
- it contains at least one special character
- it has a minimum length of 8 characters.
"""

import re

def validatePassword(password):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(pattern, password))