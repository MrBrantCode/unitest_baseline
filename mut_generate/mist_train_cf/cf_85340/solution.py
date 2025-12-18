"""
QUESTION:
Write a function `simplify_url(url)` that takes a URL string as input, removes the "http://" or "https://", and the trailing query strings, and returns the domain name. The function should handle different URL structures, including those with "www" prefix and query strings. For example, given the input 'http://www.linkedin.com/home/profile?' the function should return 'linkedin.com' and given the input 'https://www.example.com/search/results?query=example' it should return 'example.com'.
"""

from urllib.parse import urlparse

def simplify_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith("www."):
        domain = domain[4:]
    return domain