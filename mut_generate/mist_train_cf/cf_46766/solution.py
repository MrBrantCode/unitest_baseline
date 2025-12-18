"""
QUESTION:
Create a function named `match_url` that takes a string as input and returns True if the string matches the pattern "www.somedomain.com/posts/[post_id]" and False otherwise. The function should consider alphanumeric post_ids, optional query strings, and a length constraint of 5 to 10 characters for the domain name.
"""

import re

def match_url(url):
    """
    This function checks if the input URL matches the pattern 
    "www.somedomain.com/posts/[post_id]" and returns True if it does, False otherwise.
    The function considers alphanumeric post_ids, optional query strings, and a length 
    constraint of 5 to 10 characters for the domain name.

    Args:
        url (str): The URL to be matched.

    Returns:
        bool: True if the URL matches the pattern, False otherwise.
    """
    pattern = r'^www\.[a-z0-9]{5,10}\.com/posts/[\w]+(\?[\w]+=[\w]+(&[\w]+=[\w]+)*)?$'
    return bool(re.match(pattern, url))