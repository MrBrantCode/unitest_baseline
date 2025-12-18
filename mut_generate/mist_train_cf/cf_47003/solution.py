"""
QUESTION:
Write a function `extract_urls` that takes an input string and returns a list of all valid URLs that start with 'https://'. A valid URL is one that can be parsed into its components (scheme, netloc, and path) using the `urlparse` function from the `urllib.parse` module. The function should also validate the subdomain naming correctness, but for the purpose of this question, it is enough to check that the URL has a scheme, a network location (netloc), and a path.
"""

import re
from urllib.parse import urlparse

def extract_urls(input_string):
    potential_urls = re.findall('https://[^\s]*', input_string)
    valid_urls = [url for url in potential_urls if urlparse(url).scheme and urlparse(url).netloc and urlparse(url).path]
    return valid_urls