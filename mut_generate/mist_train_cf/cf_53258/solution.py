"""
QUESTION:
Create a function `user_password_check(password, username, previous_passwords)` that checks the validity of a user's password. 

The password is valid if it meets the following conditions:

- Consists of alphanumeric characters with at least two uppercase letters, two lowercase letters, and three digits.
- Contains at least one special character from ['@', '#', '$', '%', '&', '*'].
- Does not contain more than two consecutive digits.
- Does not include whitespace characters or any part of the username.
- Does not contain more than three consecutive identical characters.
- Has not been used in the last five previous passwords.
- Has a length between 12 and 50 characters.

The function should return 'Valid' if the password is valid and 'Invalid' otherwise.
"""

import re

def user_password_check(password, username, previous_passwords):
    # Check length of password
    if len(password) < 12 or len(password) > 50:
        return 'Invalid'

    # Check if password contains any part of the username 
    if username in password:
        return 'Invalid'

    # Check if password contains more than 3 consecutive identical characters
    if re.search(r'(.)\1{3,}', password):
        return 'Invalid'

    # Check if password contains special character ('@', '#', '$', '%', '&', '*')
    if not re.search(r'[@#$%&*]', password):
        return 'Invalid'

    # Check if password contains more than 2 consecutive digits 
    if re.search(r'\d{3,}', password):
        return 'Invalid'

    # Check if password has more than 1 uppercase letter
    if len(re.findall(r'[A-Z]', password)) <= 1:
        return 'Invalid'

    # Check if password has more than 1 lowercase letter
    if len(re.findall(r'[a-z]', password)) <= 1:
        return 'Invalid'

    # Check if password has more than 2 digits
    if len(re.findall(r'\d', password)) <= 2:
        return 'Invalid'

    if password in previous_passwords[-5:]:
        return 'Invalid'

    return 'Valid'