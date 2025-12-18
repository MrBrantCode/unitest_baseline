"""
QUESTION:
Create a function `validate_password` that takes a string `password` as input and returns a boolean value indicating whether the password meets the following criteria:
- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter.
- The password must contain at least one lowercase letter.
- The password must contain at least one digit.
The function should return `True` if the password is valid and `False` otherwise.
"""

def validate_password(password):
    if len(password) < 8:
        return False
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_uppercase and has_lowercase and has_digit