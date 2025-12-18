"""
QUESTION:
Write a function `validate_password(password)` that validates a given password. The password should be at least 12 characters long and contain at least two lowercase letters, two uppercase letters, two numbers, and two special characters. The password should not contain any consecutive repeating characters and should not be a common or easily guessable password. The function should return a boolean value indicating whether the password is valid or not.
"""

import re

def validate_password(password):
    # Check password length
    if len(password) < 12:
        return False
    
    # Check consecutive repeating characters
    for i in range(len(password) - 2):
        if password[i] == password[i+1] and password[i+1] == password[i+2]:
            return False
    
    # Check lowercase letters
    if len(re.findall(r'[a-z]', password)) < 2:
        return False
    
    # Check uppercase letters
    if len(re.findall(r'[A-Z]', password)) < 2:
        return False
    
    # Check numbers
    if len(re.findall(r'\d', password)) < 2:
        return False
    
    # Check special characters
    if len(re.findall(r'[^a-zA-Z0-9\s]', password)) < 2:
        return False
    
    # Check against common passwords
    common_passwords = ['password', '123456', 'qwerty', 'abc123']  # Add more common passwords here
    if password in common_passwords:
        return False
    
    return True