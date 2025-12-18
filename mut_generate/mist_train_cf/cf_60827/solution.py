"""
QUESTION:
Write a function `user_password_check(password)` that checks if a given password meets certain criteria. The password is valid if it: 
- contains alphanumeric characters with at least one uppercase, one lowercase, and one digit, 
- contains a symbol from the list ['@', '#', '$', '%', '&', '*'], 
- has a maximum of two consecutive digits, 
- does not contain whitespace characters, 
- does not contain more than two consecutive identical characters, 
- has a length between 8 and 30 characters.
The function should return 'Valid' if the password meets all the criteria and 'Invalid' otherwise.
"""

import re

def user_password_check(password):
    # Test password length
    if not 8 <= len(password) <= 30:
        return 'Invalid'
    # Test for alphanumeric characters with at least one uppercase, one lowercase, and one digit
    if not re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', password):
        return 'Invalid'
    # Test for symbol
    if not re.search(r'[@#$%&*]', password):
        return 'Invalid'
    # Test for maximum of two consecutive digits
    if re.search(r'\d{3,}', password):
        return 'Invalid'
    # Test for whitespace characters
    if re.search(r'\s', password):
        return 'Invalid'
    # Test for more than two consecutive identical characters
    if re.search(r'(.)\1{2,}', password):
        return 'Invalid'
    return 'Valid'