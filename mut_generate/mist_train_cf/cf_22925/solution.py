"""
QUESTION:
Implement a function named `is_valid_email` that checks whether the provided email address is valid. The email should contain an '@' symbol and a domain name.
"""

import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))