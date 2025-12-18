"""
QUESTION:
Write a function called `is_valid_url_length` that checks if a given URL's length is within the recommended maximum length as defined in RFC 3986 (2048 characters). The function should return True if the URL's length is within the limit and False otherwise.
"""

def is_valid_url_length(url: str) -> bool:
    """
    Checks if a given URL's length is within the recommended maximum length as defined in RFC 3986 (2048 characters).

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL's length is within the limit, False otherwise.
    """
    return len(url) <= 2048