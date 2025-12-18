"""
QUESTION:
Write a function named `validate_email` that validates an email address. The email address should be valid according to the following rules:
- It should not contain any special characters except for a dot (.) and an underscore (_) in both the local part and domain name.
- The domain name should not exceed 255 characters.
- The email address should have a valid format for subdomain(s), if present, consisting only of letters, numbers, and hyphens.
- The email address should have a valid format for domain labels, consisting only of letters.
- The email address should have a valid format for the top-level domain (TLD), consisting only of letters.
- The email address should not be from a disposable email provider based on a pre-defined list of disposable email domains.

The function should return True if the email address is valid, and False otherwise.
"""

import re

def validate_email(email):
    # Define the regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Check if the email address matches the pattern
    if not re.match(pattern, email):
        return False

    # Check if the domain name exceeds 255 characters
    domain = email.split('@')[1]
    if len(domain) > 255:
        return False

    # Check if the email address contains any special characters other than dot (.) and underscore (_)
    special_chars = set(domain) - set('.-_')
    if special_chars:
        return False

    # Check if the email address has a valid format for subdomain(s), if present
    subdomains = domain.split('.')
    for subdomain in subdomains[:-1]:
        if not re.match(r'^[a-zA-Z0-9-]+$', subdomain):
            return False

    # Check if the email address has a valid format for domain labels
    if not re.match(r'^[a-zA-Z]+$', subdomains[-1]):
        return False

    # Check if the email address has a valid format for the top-level domain (TLD)
    tld = subdomains[-1].lower()
    if not re.match(r'^[a-zA-Z]+$', tld):
        return False

    # Check if the email address is from a disposable email provider
    disposable_domains = ['example.com', 'example.org']  # Add more disposable domains to the list
    if domain in disposable_domains:
        return False

    return True