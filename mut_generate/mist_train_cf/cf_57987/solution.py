"""
QUESTION:
Write a function named `test_password_strength` that evaluates the strength of a given password. The password is considered strong if it meets the following conditions: it has a minimum length of 8 characters, contains at least one uppercase letter, one lowercase letter, one digit, and one special character. The function should return a message indicating the reason for a weak password or a confirmation of a strong password.
"""

import re

def test_password_strength(password):
    # Checking for minimum length
    if len(password) < 8:
        return "Password too short"
        
    # Checking for uppercase
    elif not re.search("[A-Z]", password):
        return "Password should include at least 1 uppercase letter"
        
    # Checking for lowercase
    elif not re.search("[a-z]", password):
        return "Password should include at least 1 lowercase letter"
        
    # Checking for digits
    elif not re.search(r"\d", password):
        return "Password should include at least 1 digit"
        
    # Checking for symbols
    elif not re.search(r"\W", password):
        return "Password should include least 1 special character"
 
    else:
        return "Password strength is strong"