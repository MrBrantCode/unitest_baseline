"""
QUESTION:
Create a Python function `is_valid_email(email)` that takes a string `email` as input and returns `True` if the email is valid and `False` otherwise. A valid email should match the standard email format protocol, i.e., it should contain letters, numbers, periods, underscores, pluses, or hyphens before the '@' symbol, followed by letters, numbers, or hyphens, and then a period and letters, numbers, periods, or hyphens. The function should use regular expressions to validate the email format.
"""

import re

def is_valid_email(email):
    # regular expression pattern for email validation
    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    return False