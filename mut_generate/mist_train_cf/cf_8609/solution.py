"""
QUESTION:
Implement a function called `is_valid_password(password)` that checks whether a given string is a valid password. A valid password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character, not contain any spaces, and not be a common password. Assume the input string only contains alphanumeric characters and special characters.
"""

def is_valid_password(password):
    common_passwords = ["password", "qwerty", "abc123"] # List of common passwords

    if len(password) >= 8:
        if any(char.isupper() for char in password):
            if any(char.islower() for char in password):
                if any(char.isdigit() for char in password):
                    if any(char in '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?' for char in password):
                        if ' ' not in password:
                            if password.lower() not in common_passwords:
                                return True
    return False