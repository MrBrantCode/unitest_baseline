"""
QUESTION:
Create a function named `email_parser` that takes an email address as input, validates its structure, and extracts the domain information. The function should return a dictionary containing the second-level domain, top-level domain, and a categorization of the domain type as either 'special' or 'normal'. Special domains include government domains (gov, edu, org) and common email providers (gmail, yahoo, outlook). If the email address is invalid, the function should return False.
"""

import re

def email_parser(email_address):
    """
    This function takes an email address as input, validates its structure, 
    and extracts the domain information. It returns a dictionary containing 
    the second-level domain, top-level domain, and a categorization of the 
    domain type as either 'special' or 'normal'. If the email address is 
    invalid, the function returns False.

    Parameters:
    email_address (str): The email address to be parsed.

    Returns:
    dict or bool: A dictionary containing the domain information or False 
                  if the email address is invalid.
    """

    # Regular expression pattern to match the email address structure
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@(?P<secondlevel>[a-zA-Z0-9-]+)\.(?P<toplevel>[a-zA-Z0-9-.]+$)")
    
    # Match the email address against the pattern
    match = pattern.match(email_address)
    
    # If the email address does not match the pattern, return False
    if match is None:
        return False

    # Determine the domain type based on the top-level and second-level domains
    if match.group('toplevel') in ['gov','edu','org'] or match.group('secondlevel') in ['gmail','yahoo','outlook']:
        domain_type = 'special'
    else:
        domain_type = 'normal'

    # Return a dictionary containing the domain information
    return {
        'secondlevel': match.group('secondlevel'),
        'toplevel': match.group('toplevel'),
        'domain_type': domain_type,
    }