"""
QUESTION:
Implement the `put_request` function that takes a URL as input and returns the URL with the PUT method incorporated. The incorporated PUT method should be appended to the end of the URL.
"""

def put_request(url):
    """
    This function takes a URL as input, appends the PUT method to it, and returns the resulting URL.

    Args:
        url (str): The input URL.

    Returns:
        str: The URL with the PUT method incorporated.
    """
    return url + '/PUT'