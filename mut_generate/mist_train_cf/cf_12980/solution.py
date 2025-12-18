"""
QUESTION:
Extract the domain name from a given URL, excluding any subdomains and paths. The function should take a string representing the URL as input and return the extracted domain name.
"""

def extract_domain(url):
    """
    Extract the domain name from a given URL, excluding any subdomains and paths.

    Args:
        url (str): The input URL.

    Returns:
        str: The extracted domain name.
    """
    from urllib.parse import urlparse
    return urlparse(url).netloc.split('.')[-2] + '.' + urlparse(url).netloc.split('.')[-1]