"""
QUESTION:
Write a function `check_string` that checks if a given string contains at least one uppercase letter, one lowercase letter, and one numeric digit. The string length must be between 6 and 20 characters and it should not contain any special characters or consecutive repeated characters.
"""

import re

def check_string(string):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?!.*(.).*\1)[a-zA-Z\d]{6,20}$'
    if re.match(pattern, string):
        return True
    return False