"""
QUESTION:
Create a regular expression pattern to match and extract URLs from strings. The pattern should be able to match both HTTP and HTTPS URLs, with or without the 'www' subdomain, and with top-level domains of at least two characters. The pattern should match URLs that have at least one alphanumeric character in the domain name. The matched URLs should be in the format 'http://example.com', 'https://example.com', 'http://www.example.com', 'https://www.example.com', 'www.example.com'.
"""

import re

def extract_urls(text):
    """
    Extracts URLs from a given text.

    Args:
    text (str): The text to extract URLs from.

    Returns:
    list: A list of extracted URLs.
    """
    pattern = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
    return re.findall(pattern, text)