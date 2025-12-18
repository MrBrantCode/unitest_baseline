"""
QUESTION:
Create a function called `validate_email(email)` that takes an email address as input and returns `True` if the email is valid and `False` otherwise. A valid email address should match the conventional structure of a typical email address, consisting of a local part followed by the `@` symbol, followed by a domain. The local part and domain should contain only alphanumeric characters, dots, underscores, pluses, and hyphens.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))