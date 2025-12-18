"""
QUESTION:
Create a function `validate_url` that takes a string as input and returns `True` if the string matches the following URL format: `https://www.example.com/path/page.html`. The function should validate that the URL starts with `https`, has `www`, has a domain with at least 2 alphabetical characters as the top-level domain, has a path and a filename with at least one alphanumeric character or hyphen, and ends with `.html`.
"""

import re

def validate_url(url):
    """
    Validate a URL in the format https://www.example.com/path/page.html.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    pattern = r"^https:\/\/www\.[a-zA-Z0-9-]+\.[a-zA-Z]{2,}\/[a-zA-Z0-9-]+\/[a-zA-Z0-9-]+\.html$"
    return bool(re.match(pattern, url))