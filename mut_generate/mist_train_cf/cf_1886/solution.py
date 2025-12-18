"""
QUESTION:
Create a function `is_valid_url` that takes a string as input and returns `True` if it is a valid URL, `False` otherwise. A valid URL starts with "https://", ends with ".com", and has at least one subdomain before the top-level domain. The subdomain must be at least 2 characters long and cannot contain consecutive dashes. The URL may contain any combination of alphanumeric characters, dashes, and dots between the subdomain and the top-level domain.
"""

import re

def is_valid_url(url):
    """
    Validate if a given string is a valid URL.
    
    A valid URL starts with "https://", ends with ".com", and has at least one subdomain before the top-level domain.
    The subdomain must be at least 2 characters long and cannot contain consecutive dashes.
    The URL may contain any combination of alphanumeric characters, dashes, and dots between the subdomain and the top-level domain.

    Args:
    url (str): The URL to be validated.

    Returns:
    bool: True if the URL is valid, False otherwise.
    """

    # Regular expression pattern to match the requirements
    pattern = r"^https://([a-zA-Z0-9]+-?)+(?!-)([a-zA-Z0-9]+)\.com$"
    
    # Use the fullmatch function to ensure the entire URL matches the pattern
    return bool(re.fullmatch(pattern, url))