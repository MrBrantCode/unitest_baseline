"""
QUESTION:
Create a function called `validate_email(email)` that takes an email address as a string and returns `True` if the email is valid and `False` otherwise. The email is considered valid if it contains a local part, the '@' symbol, a domain name, and a top-level domain, with the local part consisting of alphanumeric characters, '.', '_', '+', and '-', the domain name consisting of alphanumeric characters and '-', and the top-level domain starting with a dot '.' and consisting of alphanumeric characters, '-', and '.'.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.search(pattern, email):
        return True
    else:
        return False