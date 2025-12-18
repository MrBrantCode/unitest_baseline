"""
QUESTION:
Write a function `is_valid_email` that takes a string as input and returns the domain name if the string is a valid email address, otherwise returns `None`. The email address is considered valid if it matches the pattern `r'^[\w\.-]+@[\w\.-]+\.\w+$'`, which checks for a combination of alphanumeric characters, dots, and hyphens before the '@' symbol, and a valid domain name after the '@' symbol. The domain name should be extracted by splitting the email address at the '@' symbol.
"""

import re

def is_valid_email(email):
    # Regular expression to check if the email is valid
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        # Split the email address at the '@' symbol to extract the domain name
        domain = email.split('@')[1]
        return domain
    else:
        return None