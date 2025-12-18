"""
QUESTION:
Create a function `is_valid_email(email)` to check if a given email address is valid using Regular Expressions. The function should return `True` if the email is valid and `False` otherwise. The email address is considered valid if it matches the common email format, i.e., it contains alphanumeric characters, periods, underscores, or hyphens before the '@' symbol, followed by alphanumeric characters, periods, or hyphens after the '@' symbol, and ends with a domain extension (e.g., .com, .net, .org).
"""

import re

def is_valid_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return bool(re.search(regex, email))