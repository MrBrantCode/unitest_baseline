"""
QUESTION:
Implement the `password_check(password)` function that takes a password string as input and returns `True` if it meets the following requirements:

- The password is at least 8 characters long.
- The password contains at least one uppercase character, one lowercase character, one digit, and one special character.
- The password does not contain sequential numbers (like "1234").
- The password does not contain repeated letters (like "AAAA").
- The password is not a commonly used password (like "password").
 
Note that the function should check for these requirements in a case-sensitive manner and should return `False` as soon as any of the requirements are not met.
"""

import re

def password_check(password):
    special_characters = ['$', '@', '#', '%', '!', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '<', '>', '?', '~']
    common_passwords = ["password", "admin", "qwerty", "admin123", "password123", "123456", "111111"]
    if (len(password) < 8):
        return False
    elif not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif not any(char in special_characters for char in password):
        return False
    elif password in common_passwords:
        return False
    elif ('1234' in password) or (password[::] == password[::-1]):
        return False
    elif (re.search(r'(.)\1\1\1', password)):
        return False
    else:
        return True