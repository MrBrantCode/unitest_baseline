"""
QUESTION:
Write a function `validate_email` that takes a string as input and returns a boolean indicating whether the string is a valid email address. A valid email address should match the following rules: 
- it should contain exactly one '@' symbol, 
- it should have a top-level domain that consists of letters only and is between 2 and 5 characters long, 
- it should not contain any spaces or special characters other than '.', '_', and '-'.
"""

import re

def validate_email(email):
    pattern = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    return bool(re.match(pattern, email))