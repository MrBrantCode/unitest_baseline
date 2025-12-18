"""
QUESTION:
Create a function called `validate_url` that takes a string representing a URL as input and returns `True` if the URL is valid and `False` otherwise. A valid URL must start with either "http://" or "https://" and end with a valid domain extension such as ".com", ".org", or ".net". The function should be able to handle cases where the URL contains query parameters or additional paths after the domain.
"""

import re

def validate_url(url):
    # Check if the URL starts with "http://" or "https://"
    if not url.startswith("http://") and not url.startswith("https://"):
        return False
    # Check if the URL ends with a valid domain extension
    valid_extensions = [".com", ".org", ".net"]
    if not any(url.endswith(extension) for extension in valid_extensions):
        return False
    return True