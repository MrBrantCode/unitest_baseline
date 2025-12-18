"""
QUESTION:
Implement a function named `parse_url` that takes a URL string as input and returns a dictionary containing the extracted protocol, hostname, path, query parameters, and fragments. The function should handle URL encoding and decoding for the query parameters and include error handling for invalid URLs.
"""

from urllib.parse import urlparse, parse_qs, unquote

def parse_url(url):
    try:
        parsed_url = urlparse(url)
        
        protocol = parsed_url.scheme
        hostname = parsed_url.hostname
        path = parsed_url.path
        query = parse_qs(parsed_url.query)
        fragments = parsed_url.fragment
        
        query = {key: unquote(value[0]) for key, value in query.items()}
        
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