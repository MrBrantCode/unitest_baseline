"""
QUESTION:
Create a function `validate_email` that takes a string as input and returns a boolean indicating whether the string is a valid email address. The function should use regular expressions to match common email address formats, allowing for alphanumeric characters, certain special characters, and domain extensions. The email should be in the format 'local-part@domain', where 'local-part' can contain letters, numbers, and certain special characters, and 'domain' can contain letters, numbers, and hyphens, with optional subdomains.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    return bool(re.match(pattern, email))