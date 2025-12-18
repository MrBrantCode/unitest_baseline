"""
QUESTION:
Write a function `validate_email` that checks if the given input string is a valid email address. The input string should contain a username, a domain name, and a top-level domain, separated by '@' and '.' respectively. The username can contain alphanumeric characters and special characters '.','_','+','-'. The domain name can contain alphanumeric characters and '-'. The top-level domain can contain alphanumeric characters, '.' and '-'. The function should return True if the input string is a valid email address, otherwise False.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))