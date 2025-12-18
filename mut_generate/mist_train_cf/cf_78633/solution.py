"""
QUESTION:
Create a function `validate_password(password)` that checks if a given password meets the following requirements:

- The password must be at least 10 characters long.
- The password must contain at least one uppercase letter.
- The password must contain at least one lowercase letter.
- The password must contain at least one number.
- The password must contain at least one special symbol (~!@#$%^&*()_=-[]{};':,.<>).
- The password must not contain any sequence of 3 characters or more that are the same (e.g., "aaa" or "111").

The function should return True if the password meets all the requirements, and False otherwise.
"""

import re

def validate_password(password):
    if re.search(r'(.)\1\1', password) is not None:
        return False
    if len(password) < 10:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[~!@#$%^&*()_=-\[\]{};':,.<>]", password):
        return False

    return True