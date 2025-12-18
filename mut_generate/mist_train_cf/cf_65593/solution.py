"""
QUESTION:
Create a function called `validate_email` that uses a regular expression pattern to match an arbitrary email address in the form of "username@domain.extension". The function should match various characters used in real-world email addresses.
"""

import re

def validate_email(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(pattern, email))