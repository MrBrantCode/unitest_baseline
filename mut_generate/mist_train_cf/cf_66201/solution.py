"""
QUESTION:
Write a function `is_valid_email(email)` to verify if a given string `email` meets the standard email format using regular expressions. The function should return `True` if the email is valid and `False` otherwise. The email format should include alphanumeric characters, may contain a dot (.) or underscore (_), followed by the '@' symbol, alphanumeric characters, a dot (.), and at least a 2-3 character top-level domain.
"""

import re

def is_valid_email(email):
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return bool(re.match(email_regex, email))