"""
QUESTION:
Create a function `validate_string(string)` that checks if a given string contains at least one uppercase letter, one lowercase letter, and one numeric digit, while also ensuring that the string length is between 6 and 20 characters.
"""

import re

def validate_string(string):
    # Check length
    if len(string) < 6 or len(string) > 20:
        return False

    # Check for uppercase, lowercase, and numeric characters
    if not re.search(r"[A-Z]", string):
        return False
    if not re.search(r"[a-z]", string):
        return False
    if not re.search(r"\d", string):
        return False

    return True