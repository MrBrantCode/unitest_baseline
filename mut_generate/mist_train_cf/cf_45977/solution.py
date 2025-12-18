"""
QUESTION:
Create a function `user_password_check(password, username, previous_passwords)` that checks the complexity of a new password and returns 'Valid' if it meets all the requirements, 'Invalid' otherwise. The password is invalid if it does not meet any of the following conditions: 

- The length of the password is between 12 and 50 characters.
- The password does not contain any part of the username.
- The password does not contain more than 3 consecutive identical characters.
- The password contains at least one special character among '@', '#', '$', '%', '&', '*'.
- The password does not contain more than 2 consecutive digits.
- The password has more than 1 uppercase letter.
- The password has more than 1 lowercase letter.
- The password has more than 2 digits.
- The password is not among the last 5 used passwords.
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