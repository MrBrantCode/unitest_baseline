"""
QUESTION:
Create a function called `validate_email` that takes an email address as input and returns `True` if the email is valid and `False` otherwise. The function should consider an email address as valid if it matches the standard email format, which consists of alphanumeric characters, dot, underscore, and hyphen before the '@' symbol, followed by alphanumeric characters and a period, and ends with a 2-3 character top-level domain.
"""

import re

def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return bool(re.search(regex,email))