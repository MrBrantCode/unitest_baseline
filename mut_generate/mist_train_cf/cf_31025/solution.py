"""
QUESTION:
Create a function `validate_password(password, username)` that checks whether a given password meets certain criteria and returns True if the password is valid, and False otherwise. The password is valid if it is at least 8 characters long, contains at least one uppercase letter, one lowercase letter, and one digit, and does not contain the username as a substring.
"""

def validate_password(password, username):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if username in password:
        return False
    return True