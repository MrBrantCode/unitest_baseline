"""
QUESTION:
Write a function named `normalize_url` that takes a URL as input and returns the URL with the trailing question mark or any characters after it removed. The input URL may or may not have a trailing question mark.
"""

def normalize_url(url):
    """
    This function takes a URL as input and returns the URL with the trailing question mark or any characters after it removed.

    Args:
        url (str): The input URL

    Returns:
        str: The URL with the trailing question mark or any characters after it removed
    """
    return url.split('?')[0]