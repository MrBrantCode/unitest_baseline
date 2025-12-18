"""
QUESTION:
Write a function called `is_valid_email` that takes a string as input and returns `True` if the string is a valid email address and `False` otherwise. The function should use a regular expression to match the standard email address format, which consists of alphanumeric characters, special characters, and a domain name with optional subdomains.
"""

import re

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    return bool(re.match(regex, email))