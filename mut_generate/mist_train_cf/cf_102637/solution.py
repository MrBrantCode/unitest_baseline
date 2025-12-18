"""
QUESTION:
Write a function named `validate_password(password)` that takes a string password as input and returns `True` if the password is valid and `False` otherwise. A password is considered valid if its length is at least 8 characters and at most 20 characters. If the password is too short or too long, print an error message indicating the reason.
"""

def validate_password(password):
    if len(password) < 8:
        print("Password is too short")
        return False
    elif len(password) > 20:
        print("Password is too long")
        return False
    else:
        return True