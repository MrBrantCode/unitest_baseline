"""
QUESTION:
Create a function `validate_email(email)` that checks the validity of an email address. The function should enforce the following rules: 
- The email address must have a minimum length of 12 characters and a maximum length of 200 characters. 
- It should contain an "@" symbol. 
- The domain name should have at least 4 characters and at least two dots (.). 
- The characters after each dot in the domain name should be letters only. 
- The local part (before the "@" symbol) should not contain special characters other than ".", "-", "_", and it should not start or end with these special characters, nor contain consecutive special characters.
"""

import re

def validate_email(email):
    # Check length of email address
    if len(email) < 12 or len(email) > 200:
        return False

    # Check for "@" symbol
    if "@" not in email:
        return False

    # Split email address into local part and domain part
    local_part, domain_part = email.split("@", 1)

    # Check length of domain name
    if len(domain_part) < 4:
        return False

    # Check for special characters in local part
    if re.search(r'[^A-Za-z0-9_.-]', local_part[1:-1]):
        return False

    # Check for consecutive special characters in local part
    if re.search(r'[_.-]{2,}', local_part):
        return False

    # Check for special characters at the start or end of local part
    if local_part.startswith('.') or local_part.startswith('-') or local_part.startswith('_'):
        return False
    if local_part.endswith('.') or local_part.endswith('-') or local_part.endswith('_'):
        return False

    # Check for valid format of domain name
    if domain_part.count('.') < 2:
        return False
    for part in domain_part.split('.'):
        if not part.isalpha():
            return False

    return True