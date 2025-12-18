"""
QUESTION:
Implement a function `validate_email(email)` that takes an email address as a string and returns `True` if the email address is valid and `False` otherwise, based on the following criteria:
- The email address must contain exactly one "@" symbol.
- The "@" symbol must not be the first or last character of the email address.
- The email address must contain at least one "." after the "@" symbol.
- The characters before and after the "@" symbol must not contain any spaces.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))