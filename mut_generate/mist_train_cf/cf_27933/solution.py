"""
QUESTION:
Implement the `validate_password` function that takes a password as input and returns "Password is valid." if the password meets the following criteria:
- The password contains at least 8 characters.
- The password contains at least one uppercase letter, one lowercase letter, one digit, and one special character from the set {!, @, #, $, %, ^, &, *}.

The function should return "Password is invalid." if the password does not meet these criteria.
"""

import re

def validate_password(password):
    if len(password) < 8 or not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'\d', password) or not re.search(r'[!@#$%^&*]', password):
        return "Password is invalid."
    return "Password is valid."