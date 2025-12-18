"""
QUESTION:
Implement a function `validate_password(password)` that checks if a given password is valid based on the following criteria: 
- The password length is between 8 and 16 characters.
- The password contains at least one uppercase character.
- The password contains at least one lowercase character.
- The password contains at least one digit.
- The password contains at least one special character.
- The password does not contain any spaces.

Return True if the password is valid and False otherwise.
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