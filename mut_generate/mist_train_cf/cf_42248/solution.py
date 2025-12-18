"""
QUESTION:
Create a function called `is_valid_email` that takes a string `email` as input and returns True if it matches the standard email format of "username@domain.extension", where the username can contain letters, numbers, periods, hyphens, and underscores, the domain can contain letters and hyphens, and the extension can contain letters with a length of 2 to 4 characters, and False otherwise.
"""

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))