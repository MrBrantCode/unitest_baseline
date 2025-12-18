"""
QUESTION:
Write a function `validate_email(email)` that takes an email address as input and returns a boolean indicating whether the email address is valid and its domain name has a valid top-level domain (TLD). A valid TLD is defined as a sequence of at least two alphabetic characters. The function should check the format of the email address and its TLD using regular expressions.
"""

import re

def validate_email(email):
    # Regular expression to validate email address format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Check if email address format is valid
    if not re.match(email_regex, email):
        return False
    
    # Extract domain name from email address
    domain = email.split('@')[1]
    
    # Regular expression to validate TLD format
    tld_regex = r'^[a-zA-Z]{2,}$'
    
    # Check if domain name has a valid TLD format
    if not re.match(tld_regex, domain.split('.')[-1]):
        return False
    
    return True