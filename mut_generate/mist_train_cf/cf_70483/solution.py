"""
QUESTION:
Develop a function "parse_urls" that takes a URL string as input and returns a dictionary containing the query parameters of the URL. The returned dictionary should only include the first value for each key.
"""

from urllib.parse import urlparse, parse_qs

def parse_urls(url):
    query = urlparse(url).query
    params = parse_qs(query)
    return {k: v[0] for k, v in params.items()}