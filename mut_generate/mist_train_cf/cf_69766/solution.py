"""
QUESTION:
Design a function named `parse_url` that takes a URL string as input and returns a dictionary with the URL's components, including scheme, netloc, path, and query parameters. The function should validate the URL structure, adhering to standard URL syntax, and handle URLs with complex query parameters and multiple sub-paths. The function should return "Invalid URL" if the input URL is invalid. Assume a URL is valid only if it has a scheme and a netloc.
"""

import urllib.parse

def parse_url(url):
    # check if the URL is valid
    try:
        parsed_url = urllib.parse.urlparse(url)
    except ValueError:
        return "Invalid URL"

    # Check if URL has necessary components
    if not all([parsed_url.scheme, parsed_url.netloc]):
        return "Invalid URL"

    # parse query params
    queries = urllib.parse.parse_qs(parsed_url.query)

    return {
        'scheme': parsed_url.scheme,
        'netloc': parsed_url.netloc,
        'path': parsed_url.path,
        'params': queries
    }