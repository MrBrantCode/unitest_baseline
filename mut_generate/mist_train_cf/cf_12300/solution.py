"""
QUESTION:
Write a function named `validate_password(password)` that takes a string `password` as input and returns a boolean value indicating whether the password is valid or not. A password is valid if it meets the following conditions: it is at least 8 characters long, contains at least one lowercase letter, one uppercase letter, one number, and one special character, and does not contain any consecutive repeating characters.
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