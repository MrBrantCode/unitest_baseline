"""
QUESTION:
Create a Python function named `validate_urls` that takes a list of URLs as input. The function should ensure each URL has either 'http' or 'https' scheme and a non-empty network location. If any URL is found to be invalid, the function should return False. If all URLs are valid, the function should return True.
"""

import urllib.parse

def validate_urls(urls):
    """
    Validate a list of URLs.

    Args:
    urls (list): A list of URLs to validate.

    Returns:
    bool: True if all URLs are valid, False otherwise.
    """
    for url in urls:
        parsed = urllib.parse.urlparse(url)
        if not (parsed.scheme in ('http', 'https') and parsed.netloc):
            return False
    return True