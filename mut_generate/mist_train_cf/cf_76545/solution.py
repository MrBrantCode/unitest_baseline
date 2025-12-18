"""
QUESTION:
Create a function named `verify_email(email)` that takes a string `email` as input and returns `True` if the email address matches the common email address syntax and `False` otherwise. The syntax should include alphanumeric characters, underscores, dots, plus signs, or dashes before the '@' symbol, followed by alphanumeric characters, dashes, or dots, and ending with a domain that starts with a dot and is followed by alphanumeric characters or dashes.
"""

import re

def verify_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return bool(pattern.match(email))