"""
QUESTION:
Create a function called `validate_email(email, allowed_domains)` that verifies an email address using regular expressions. The function should check if the email address matches the following criteria: 
- The username (before '@') is 5-30 characters long and contains only alphanumeric characters, dots, and underscores.
- The domain is valid and corresponds to a domain in the `allowed_domains` list.
 
The function should return `True` if the email is valid and `False` otherwise.
"""

import re

def validate_email(email, allowed_domains):
    pattern = re.compile(r'[A-Za-z0-9\._]{5,30}[@][A-Za-z]{1,30}[.][A-Za-z]{2,4}')
    match = pattern.match(email)

    if match is None:
        return False
    
    username, domain = email.split('@')
    
    if domain not in allowed_domains:
        return False
     
    return True