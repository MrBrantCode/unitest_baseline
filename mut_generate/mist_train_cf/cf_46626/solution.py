"""
QUESTION:
Write a function `validate_domain` that checks if a given string is a valid domain name. The domain name should be 2-30 characters long, contain only alphanumeric characters, and may include a single hyphen that separates two groups of alphanumeric characters. The hyphen should not be at the beginning or end of the string.
"""

import re

def validate_domain(domain):
    """
    Checks if a given string is a valid domain name.
    
    A valid domain name should be 2-30 characters long, contain only alphanumeric 
    characters, and may include a single hyphen that separates two groups of 
    alphanumeric characters. The hyphen should not be at the beginning or end of the string.
    
    Parameters:
    domain (str): The domain name to be validated.
    
    Returns:
    bool: True if the domain name is valid, False otherwise.
    """
    # Check if the domain name is 2-30 characters long
    if len(domain) < 2 or len(domain) > 30:
        return False
    
    # Check if the domain name contains only alphanumeric characters and a single hyphen
    pattern = re.compile(r'^([a-z0-9]{1,29}-?[a-z0-9]{0,29})$')
    if not pattern.match(domain):
        return False
    
    # Check if the domain name starts or ends with a hyphen
    if domain[0] == '-' or domain[-1] == '-':
        return False
    
    return True