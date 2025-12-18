"""
QUESTION:
Write a function `validate_password(password)` that checks if a given password is valid based on the following conditions: 
- It contains at least one lowercase letter.
- It contains at least one uppercase letter.
- It contains at least one number.
- It contains at least one special character.
- Its length is at least 8 characters.
- It does not contain any consecutive repeating characters.
"""

import re

def validate_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check lowercase, uppercase, number, and special character
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not re.search(r"[!@#$%^&*()_\-+={}\[\]|\\;:'\",<.>/?]", password):
        return False
    
    # Check consecutive repeating characters
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return False
    
    # All checks passed
    return True