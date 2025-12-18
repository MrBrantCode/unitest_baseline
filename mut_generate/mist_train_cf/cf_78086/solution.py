"""
QUESTION:
Create a function `verify_email` that takes a string as input and returns `True` if the string is a valid email address and `False` otherwise, using a regular expression pattern that adheres to the standardized email address protocol.
"""

import re

def verify_email(email):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.match(pattern, email):
        return True
    else:
        return False