"""
QUESTION:
Write a function `get_domain_name(email: str) -> str` that takes in a string `email` and returns the domain name of the email address if it is valid; otherwise, returns an empty string.

The email address is valid if it contains exactly one "@" symbol, has at least one character before and after the "@" symbol, has at least one "." symbol after the "@" symbol, and consists of alphanumeric characters and special characters allowed in an email address. Additionally, the domain name must have at least one character before the first "." symbol and at least one character after the last "." symbol, and cannot contain consecutive periods.
"""

def get_domain_name(email: str) -> str:
    """
    This function takes in a string email and returns the domain name of the email address if it is valid; 
    otherwise, returns an empty string.
    
    A valid email address is one that contains exactly one "@" symbol, has at least one character before and 
    after the "@" symbol, has at least one "." symbol after the "@" symbol, and consists of alphanumeric 
    characters and special characters allowed in an email address. Additionally, the domain name must have 
    at least one character before the first "." symbol and at least one character after the last "." symbol, 
    and cannot contain consecutive periods.
    """
    
    # Check if the email address contains exactly one "@" symbol
    if email.count('@') != 1:
        return ""

    # Split the email address into username and domain name
    username, domain = email.split('@')

    # Check if both the username and domain name have at least one character
    if len(username) < 1 or len(domain) < 1:
        return ""

    # Check if the domain name has at least one "." symbol
    if '.' not in domain:
        return ""

    # Check if the domain name has at least one character before the first "." symbol and at least one character after the last "." symbol
    if domain.split('.')[0] == '' or domain.split('.')[-1] == '':
        return ""

    # Check if the domain name contains consecutive periods
    if '..' in domain:
        return ""

    # Return the domain name if all conditions are met
    return domain