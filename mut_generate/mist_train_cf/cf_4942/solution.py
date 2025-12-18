"""
QUESTION:
Write a function named `validate_password` that takes a password as input and returns a boolean value indicating whether the password is valid or not. The password is valid if it meets the following conditions: 
- it is at least 12 characters long, 
- it contains at least two lowercase letters, 
- it contains at least two uppercase letters, 
- it contains at least two numbers, 
- it contains at least two special characters, 
- it does not contain any consecutive repeating characters (i.e., the same character repeated three or more times in a row), 
- and it is not in a list of common or easily guessable passwords.
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