"""
QUESTION:
Create a function `validatePassword(password)` that takes a string `password` as input. The password is valid if it contains at least one lowercase letter (a-z), one digit (0-9), one uppercase letter (A-Z), one special character ($#@), and has a minimum length of 6 characters. The function should return `True` if the password meets all the criteria and `False` otherwise.
"""

def validatePassword(password: str) -> bool:
    if len(password) < 6:
        return False
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in ['$','#','@'] for c in password)
    return has_lowercase and has_uppercase and has_digit and has_special