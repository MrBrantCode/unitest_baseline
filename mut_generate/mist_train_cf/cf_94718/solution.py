"""
QUESTION:
Write a function `validate_string` that takes a string as input and returns `True` if the string contains only alphabets, at least one uppercase letter, at least one lowercase letter, at least one special character, and at least one digit. Otherwise, return `False`.
"""

import re

def validate_string(string):
    if not string.isalpha():
        return False
    if not any(char.isupper() for char in string):
        return False
    if not any(char.islower() for char in string):
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>0-9]", string):
        return False
    return True