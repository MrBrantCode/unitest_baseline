"""
QUESTION:
Write a function `validate_email` that uses a regular expression to validate email addresses. The function should accept a string as input and return `True` if the string is a valid email address, and `False` otherwise. The regular expression should match most common email address formats.
"""

import re

def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$"
    return bool(re.match(pattern, email))