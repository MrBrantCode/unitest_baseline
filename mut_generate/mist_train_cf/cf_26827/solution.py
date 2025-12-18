"""
QUESTION:
Implement a function `validate_password_strength(password: str) -> bool` that takes a string `password` as input and returns `True` if the password meets the following strength criteria, and `False` otherwise:
- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character from the set {!, @, #, $, %, ^, &, *}.
"""

import re

def validate_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[!@#$%^&*]", password):
        return False

    return True