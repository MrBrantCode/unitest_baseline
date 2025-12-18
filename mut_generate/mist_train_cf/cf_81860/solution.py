"""
QUESTION:
Create a function named `valid_email` that takes an email address as input and returns `True` if the email is valid, `False` otherwise. The function should validate the email address using the following rules:
- The email address should contain only lowercase letters, numbers, and special symbols (., _, @).
- The email address should be in the correct format (local-part@domain).
- The domain should be one of the specified valid domains ('gmail.com', 'yahoo.com', 'hotmail.com').
- The local-part should contain only lowercase letters.
"""

import re

def valid_email(email):
    valid_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.match(pattern, email):
        return False
    if email.split('@')[1] not in valid_domains:
        return False
    
    return True