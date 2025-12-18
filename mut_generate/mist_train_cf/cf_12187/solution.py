"""
QUESTION:
Create a function called `validate_email(email)` that takes an email address as input and returns `True` if the email is valid and `False` otherwise. The email is considered valid if it contains exactly one "@" symbol, the domain name has at least one period, and the email does not contain any special characters other than underscores, periods, and hyphens. The function should also check if the email address is not already present in a given list of existing email addresses.
"""

import re

def validate_email(email, existing_emails):
    # Check if email has '@' symbol
    if email.count('@') != 1:
        return False
    
    # Split email into local and domain parts
    local_part, domain_part = email.split('@')
    
    # Check if domain has at least one period
    if '.' not in domain_part:
        return False
    
    # Check if email contains special characters
    if not re.match("^[a-zA-Z0-9_.-]+$", email):
        return False
    
    # Check if email is already registered in the database
    if email in existing_emails:
        return False
    
    # If all checks pass, email is valid
    return True