"""
QUESTION:
Extract the domain from a URL using regex if the domain is a subdomain of ".com" and has at least two subdomains before it. The function should handle cases where the URL is missing the protocol and where the URL includes query parameters. The function should return the domain as a string.
"""

import re

def extract_domain(url):
    """
    Extract the domain from a URL using regex if the domain is a subdomain of ".com" and has at least two subdomains before it.

    Args:
        url (str): The URL to extract the domain from.

    Returns:
        str: The extracted domain if it meets the conditions, otherwise None.
    """
    pattern = r"(?:https?:\/\/)?(?:\w+\.)+(?:\w+)(?=(?:\/|\?|$))"
    match = re.search(pattern, url)
    if match:
        domain = match.group(0)
        if domain.endswith(".com") and domain.count('.') >= 2:
            return domain
    return None