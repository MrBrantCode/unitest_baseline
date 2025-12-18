"""
QUESTION:
Create a function `match_email` that takes an email address as input and returns `True` if it matches the following criteria and `False` otherwise: 
- The email address starts with one or more alphanumeric characters.
- It may have a period or underscore followed by more alphanumeric characters.
- It has a @ symbol followed by one or more word characters.
- It ends with either .org or .net in lowercase.
Do not consider uppercase characters as valid matches.
"""

import re

def match_email(email):
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.](org|net)$'
    return bool(re.search(pattern, email))