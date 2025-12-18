"""
QUESTION:
Create a function `create_url(subdomain, domain, path)` to generate a URL with the following constraints: 

The URL must start with the protocol "https://", the subdomain can only contain lowercase letters and digits and must be 3-10 characters long, the domain can only contain lowercase letters, and the path must start with a forward slash ("/") and can contain any combination of lowercase letters, digits, and hyphens ("-") with a minimum length of 5 characters.
"""

import re

def create_url(subdomain, domain, path):
    """
    Creates a URL with the given subdomain, domain, and path.
    
    The URL must start with the protocol "https://", the subdomain can only contain 
    lowercase letters and digits and must be 3-10 characters long, the domain can 
    only contain lowercase letters, and the path must start with a forward slash ("/") 
    and can contain any combination of lowercase letters, digits, and hyphens ("-") 
    with a minimum length of 5 characters.
    
    Args:
        subdomain (str): The subdomain of the URL.
        domain (str): The domain of the URL.
        path (str): The path of the URL.
    
    Returns:
        str: The generated URL if the input is valid, otherwise None.
    """

    # Validate subdomain
    if not re.match('^[a-z0-9]{3,10}$', subdomain):
        return None

    # Validate domain
    if not re.match('^[a-z]+$', domain):
        return None

    # Validate path
    if not re.match('^\/[a-z0-9-]{5,}$', path):
        return None

    # Create and return the URL
    return f"https://{subdomain}.{domain}{path}"