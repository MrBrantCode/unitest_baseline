"""
QUESTION:
Create a function `is_valid_url` that takes a string as input and returns `True` if the string is a valid URL, `False` otherwise. A valid URL should match the pattern: it starts with 'http://' or 'https://', followed by at least one alphanumeric character, dot, or hyphen, then a domain extension of 2-6 alphabetic characters, and optionally followed by any number of path segments consisting of alphanumeric characters, dots, hyphens, or spaces, and ends with an optional '/'.
"""

import re

def is_valid_url(url):
    """
    Checks if a given string is a valid URL.
    
    A valid URL should match the pattern: it starts with 'http://' or 'https://', 
    followed by at least one alphanumeric character, dot, or hyphen, then a domain 
    extension of 2-6 alphabetic characters, and optionally followed by any number of 
    path segments consisting of alphanumeric characters, dots, hyphens, or spaces, 
    and ends with an optional '/'.

    Args:
    url (str): The URL to be validated.

    Returns:
    bool: True if the URL is valid, False otherwise.
    """
    pattern = r"^(https?:\/\/)([\da-zA-Z\.-]+)\.([a-zA-Z\.]{2,6})([\/\w \.-]*)*\/?$"
    return bool(re.match(pattern, url))