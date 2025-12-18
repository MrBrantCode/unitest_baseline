"""
QUESTION:
Create a function called `validatePassword` that validates the strength of a given password. The password is valid if it meets the following requirements: 
- The password must be at least 12 characters long.
- The password must contain at least one uppercase letter.
- The password must contain at least one lowercase letter.
- The password must contain at least one number.
- The password must contain at least one special character (!@#$%^&*()_+-=[]{};:'\"\\|,.<>?).
- The password cannot contain the user's username or parts of their email.

The function should return a boolean value indicating whether the password is valid or not. The function should take three parameters: `password`, `username`, and `email`.
"""

import re

def validatePassword(password, username, email):
    if len(password) < 12:
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not any(c in '!@#$%^&*()_+-=[]{};:\'\"\\|,.<>/?' for c in password):
        return False

    if username.lower() in password.lower():
        return False

    if email.lower() in password.lower():
        return False

    return True