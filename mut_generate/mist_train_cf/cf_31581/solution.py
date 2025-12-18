"""
QUESTION:
Write a function `validate_email` that takes a string as input and returns `True` if the input is a valid email address and `False` otherwise. A valid email address follows the standard format of local-part@domain, where the local-part can contain alphanumeric characters, dots, hyphens, and underscores, the domain can contain alphanumeric characters and hyphens, and the top-level domain (TLD) consists of 2-4 alphabetic characters and is separated by at least one dot from the domain.
"""

import re

def validate_email(email):
    regex = r'^[\w.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(regex, email))