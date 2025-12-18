"""
QUESTION:
Create a function `extract_domain` that takes a URL as input and returns the domain if it is a subdomain of ".com" and has at least two subdomains before it. The function should handle cases where the URL is missing the protocol and where the URL includes query parameters. The domain should include all subdomains and the top-level domain. Use regex to solve this problem.
"""

import re

def extract_domain(url):
    """
    Extract the domain from a URL if it is a subdomain of ".com" and has at least two subdomains before it.
    
    Parameters:
    url (str): The URL to extract the domain from.
    
    Returns:
    str: The extracted domain if it meets the conditions, otherwise None.
    """
    pattern = r"(?:https?:\/\/)?((?:\w+\.){2,}com)(?=(?:\/|\?|$))"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None