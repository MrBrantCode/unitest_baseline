"""
QUESTION:
Create a function `validate_email` that takes a string as input and returns True if the input string is a valid email address in the standard format of "username@domain.extension", where the username can contain letters, numbers, dots, hyphens, and underscores, the domain can contain letters and numbers, and the extension contains only letters with a length of 2 to 4 characters.
"""

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))