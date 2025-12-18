"""
QUESTION:
Write a function named `parse_url` that takes a URL string as an input and returns a dictionary containing the protocol, hostname, path, query parameters, and fragments of the URL. The function should handle URL encoding and decoding for query parameters and include error handling for invalid URLs.
"""

from urllib.parse import urlparse, parse_qs, unquote

def parse_url(url):
    try:
        parsed_url = urlparse(url)
        protocol = parsed_url.scheme
        hostname = parsed_url.hostname
        path = parsed_url.path
        query = parse_qs(parsed_url.query)
        query = {key: unquote(value[0]) for key, value in query.items()}
        fragments = parsed_url.fragment
        
        return {
            'protocol': protocol,
            'hostname': hostname,
            'path': path,
            'query': query,
            'fragments': fragments
        }
    except Exception as e:
        print('Error parsing URL:', str(e))
        return None