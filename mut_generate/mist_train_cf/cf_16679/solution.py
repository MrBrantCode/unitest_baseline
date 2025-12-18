"""
QUESTION:
Create a function `validate_email(email)` that takes a string `email` as input and returns a boolean value. The function should validate the email address according to the following criteria: 
- the email address must start with a string of alphanumeric characters, followed by the "@" symbol, 
- the "@" symbol must be followed by a domain name consisting of a string of alphanumeric characters, followed by a dot, 
- the dot must be followed by a top-level domain (TLD) consisting of a string of 2 or 3 alphanumeric characters, 
- the string before the "@" symbol cannot contain any special characters except for "." and "_", 
- the domain name must not exceed 63 characters, 
- the email address cannot be longer than 254 characters.
"""

import re

def validate_email(email):
    if len(email) > 254:
        return False

    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,3}$'
    if re.match(pattern, email):
        username, domain = email.split('@')
        if len(username) > 64 or len(domain) > 63:
            return False
        return True
    
    return False