"""
QUESTION:
Create a function named `is_valid_email` that takes one string argument `email` and returns a boolean value indicating whether the provided email address is syntactically correct. The function should use a regular expression to check for the basic components of an email address, including username, '@' symbol, domain name, and a top-level domain.
"""

import re

def is_valid_email(email):
    regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.search(regex,email):
        return True
    else:
        return False