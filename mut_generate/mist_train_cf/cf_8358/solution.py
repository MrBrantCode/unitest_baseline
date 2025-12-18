"""
QUESTION:
Create a function named `validate_email` that takes one argument `email`. The function should return `True` if the email address is valid and `False` otherwise. The email address is valid if it meets the following criteria:
- Its length is between 12 and 200 characters.
- It contains exactly one "@" symbol.
- The domain name has at least 4 characters and at least two dots (.), with letters only after each dot.
- The local part (before the "@" symbol) does not start or end with ".", "-", or "_", does not contain consecutive special characters, and only contains letters, numbers, ".", "-", and "_".
"""

import re

def validate_email(email):
    # Check length of email address
    if len(email) < 12 or len(email) > 200:
        return False

    # Check for "@" symbol
    if email.count("@") != 1:
        return False

    # Split email address into local part and domain part
    local_part, domain_part = email.split("@", 1)

    # Check length of domain name
    if len(domain_part) < 4:
        return False

    # Check for special characters in local part
    if re.search(r'[^A-Za-z0-9_.-]', local_part):
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