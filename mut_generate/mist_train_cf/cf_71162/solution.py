"""
QUESTION:
Create a function named `create_url` that takes a subdomain, a main domain, a list of path segments, and an optional dictionary of query parameters as input, and returns a comprehensive internet URL using the HTTPS protocol. The function should correctly include the provided subdomain, main domain, and all the path segments in the correct order, and handle any potential special characters within the provided path segments and query parameters.
"""

from urllib.parse import urlencode, urlunsplit

def create_url(subdomain, domain, paths, queries=None):
    netloc = '{}.{}'.format(subdomain, domain)
    path = '/'.join(paths)
    query = ""

    if queries:
        query = urlencode(queries)
        
    scheme = 'https'

    return urlunsplit((scheme, netloc, path, query, ''))