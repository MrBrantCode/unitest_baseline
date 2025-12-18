"""
QUESTION:
Write a function `is_valid_email(email)` that uses a regular expression pattern to verify if the given string `email` is a valid email address. The pattern should match the formal email standards, including multi-level domains and special characters. The function should return `True` if the email is valid and `False` otherwise.
"""

import re

def is_valid_email(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(pattern, email))