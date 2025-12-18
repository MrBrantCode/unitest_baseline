"""
QUESTION:
Develop a function `match_url` that takes a string as input and returns `True` if the string is a valid URL, and `False` otherwise. The function should match most common URL formats, including HTTP, HTTPS, and FTP protocols, and support domain names, ports, paths, and query strings.
"""

import re

def match_url(url):
    """
    Checks if a given string is a valid URL.
    
    Args:
    url (str): The string to check.
    
    Returns:
    bool: True if the string is a valid URL, False otherwise.
    """
    pattern = r"^(https?|ftp):\/\/([a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}|localhost)(:\d{2,5})?(\/[a-zA-Z0-9._%+-\/\?=&#]*)?$"
    return bool(re.match(pattern, url))