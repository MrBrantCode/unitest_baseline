"""
QUESTION:
Create a function `is_valid_password(password)` that checks if a given password is valid. The password is valid if it contains at least one capitalized alphabet, one non-capitalized alphabet, one numerical value, and one distinctive symbol. The password must not contain any whitespace characters.
"""

import re

def is_valid_password(password):
    has_capital = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'\W', password) is not None
    
    has_no_whitespace = re.search(r'\s', password) is None
    
    return has_capital and has_lower and has_digit and has_special and has_no_whitespace