"""
QUESTION:
Create a function `validate_string` that takes a string as input and returns `True` if the string meets the following conditions and `False` otherwise:
- The length of the string is between 6 and 20 characters (inclusive).
- The string contains at least one uppercase letter, one lowercase letter, and one numeric digit.
- The string only contains alphanumeric characters (letters and digits).
"""

import re

def validate_string(s):
    # Check length
    if len(s) < 6 or len(s) > 20:
        return False

    # Check for uppercase, lowercase, and numeric characters
    if not re.search(r"[A-Z]", s):
        return False
    if not re.search(r"[a-z]", s):
        return False
    if not re.search(r"\d", s):
        return False

    # Check for alphanumeric characters
    if not re.match("^[A-Za-z0-9]*$", s):
        return False

    return True