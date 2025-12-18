"""
QUESTION:
Write a function `validate_email` that takes an email address as input and returns `True` if the email is valid, and `False` otherwise. A valid email must contain at least one uppercase letter and one number in the username part of the email address, and must not contain the domain "gmail.com" or "yahoo.com".
"""

import re

def validate_email(email):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?!.*@(?:gmail\.com|yahoo\.com))\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return bool(re.match(pattern, email))