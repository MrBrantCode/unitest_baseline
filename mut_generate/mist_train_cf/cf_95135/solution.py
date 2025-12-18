"""
QUESTION:
Write a function named `validate_email` that validates an email address. The function should check if the email address has a valid format, if the domain name has a valid top-level domain (TLD), and if the email address is from a disposable email provider. The function should return `True` if the email address is valid and not from a disposable email provider, and `False` otherwise. The function should be able to be used with various valid TLDs and disposable email providers.
"""

import re

def validate_email(email):
    # Regular expression pattern for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Regular expression pattern for disposable email providers
    disposable_regex = r'@(?:10minutemail|guerrillamail|mailinator)\.[a-zA-Z]{2,}$'
    
    # Validate email address format
    if not re.match(email_regex, email):
        return False
    
    # Check if email domain has a valid TLD
    domain = email.split('@')[1]
    tld = domain.split('.')[-1]
    valid_tlds = ['com', 'net', 'org']  # Add more valid TLDs as needed
    
    if tld not in valid_tlds:
        return False
    
    # Check if email domain is from a disposable email provider
    if re.search(disposable_regex, email):
        return False
    
    return True