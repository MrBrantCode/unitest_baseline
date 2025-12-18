"""
QUESTION:
Write a function `validate_password` that takes a string `password` as input and returns a boolean value indicating whether the password is valid or not. A valid password should contain at least 1 uppercase character, 1 lowercase character, 1 digit, and 1 special character, be between 8 and 16 characters in length (inclusive), and not contain any spaces.
"""

def validate_password(password):
    if len(password) < 8 or len(password) > 16:
        return False

    if ' ' in password:
        return False

    hasUppercase = False
    hasLowercase = False
    hasDigit = False
    hasSpecialChar = False

    for char in password:
        if char.isupper():
            hasUppercase = True
        elif char.islower():
            hasLowercase = True
        elif char.isdigit():
            hasDigit = True
        else:
            hasSpecialChar = True

    if not (hasUppercase and hasLowercase and hasDigit and hasSpecialChar):
        return False

    return True