"""
QUESTION:
Write a function `is_valid_email` to match a valid email address format using a regular expression. The function should return True for a valid email address and False otherwise. The email address is valid if it contains alphanumeric characters, dots, underscores, plus signs, or hyphens before the '@' symbol, followed by alphanumeric characters or hyphens after the '@' symbol, and then a dot followed by alphanumeric characters, dots, or hyphens.
"""

import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))