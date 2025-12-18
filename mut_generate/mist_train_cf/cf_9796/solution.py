"""
QUESTION:
Create a function called `is_valid_email` that checks if a given string is a valid email address. The email address must start with a combination of alphanumeric characters, dots, underscores, or hyphens, contain the "@" symbol, and have a domain name that starts with a combination of alphanumeric characters and contains at least one dot. The domain name cannot end with a dot and the email address cannot end with a dot. The length of the username should be between 1 and 64 characters, and the length of the domain name should be between 1 and 255 characters.
"""

import re

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._-]{1,64}@[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None