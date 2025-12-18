"""
QUESTION:
Create a function `is_valid_email(email)` that checks if a given string is a valid email address. The email address should start with a combination of alphanumeric characters, dots, underscores, or hyphens, followed by the "@" symbol, a domain name with at least one dot, and not end with a dot. The username should be between 1 and 64 characters long, and the domain name should be between 1 and 255 characters long.
"""

import re

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._-]{1,64}@[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None