"""
QUESTION:
Write a function `validate_email` that uses a regular expression to match a valid email address. The function should match one or more alphanumeric characters, dots, underscores, plus signs, or hyphens, followed by the '@' symbol, then one or more alphanumeric characters or hyphens, a dot, and finally one or more alphanumeric characters, dots, or hyphens. The email address should only be considered valid if it matches this pattern from start to end.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))