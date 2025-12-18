"""
QUESTION:
Write a function `count_url_schemes` that takes a string of text as input, extracts all URLs embedded within the text, counts the total number of each unique URL scheme, and returns a dictionary with the URL schemes as keys and their respective counts as values. The function should handle various URL formats, including protocol-specific part, authoritative part, path, and optional query string and fragment identifiers, and should implement error handling for invalid URL formats.
"""

import re
from urllib.parse import urlparse

def count_url_schemes(text):
    """
    Extracts all URLs embedded within the text, counts the total number of each unique URL scheme,
    and returns a dictionary with the URL schemes as keys and their respective counts as values.

    Args:
    text (str): The input text containing URLs.

    Returns:
    dict: A dictionary with URL schemes as keys and their counts as values.
    """
    urls = re.findall('(?P<url>https?://[^\s]+)', text)
    schemes = [urlparse(url).scheme for url in urls]
    return {scheme: schemes.count(scheme) for scheme in set(schemes)}