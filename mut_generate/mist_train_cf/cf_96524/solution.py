"""
QUESTION:
Create a function named `is_valid_email` that takes a string representing an email address. The function should return `True` if the email is valid and `False` otherwise. The email is valid if it follows the format "username@domain.com" where the username starts and ends with a letter or number, contains only lowercase letters, numbers, periods, underscores, and hyphens, and the domain has at least two levels separated by periods, with each level containing only lowercase letters and hyphens. Additionally, the domain must be a valid registered domain and not a generic top-level domain (gTLD) or a country code top-level domain (ccTLD). The function should not rely on external libraries or APIs for domain validation, but instead use a predefined list of valid registered domains.
"""

import re

def is_valid_email(email):
    # Regular expression pattern for the email format
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9]@[a-z-]+(?:\.[a-z-]+)+$'
    
    # Check if the email matches the required format
    if not re.match(pattern, email):
        return False
    
    # Split the email into username and domain
    username, domain = email.split('@')
    
    # Check if the domain is a valid registered domain
    valid_domains = ['com', 'net', 'org', 'gov']  # example list of valid domains
    domain_levels = domain.split('.')
    if len(domain_levels) < 2 or domain_levels[-1] not in valid_domains:
        return False
    
    # Check if each domain level is valid
    for level in domain_levels:
        if not re.match(r'^[a-z-]+$', level):
            return False
    
    return True