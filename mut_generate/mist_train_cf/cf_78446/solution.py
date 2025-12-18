"""
QUESTION:
Create a function `create_url` that constructs a URL from individual components. The function should handle secure (https) and non-secure (http) protocols, multiple subdomains, different domains, multiple paths, query parameters, and fragments. The function should properly encode the URL according to RFC1738 and RFC3986 Uniform Resource Locators (URL) specification.

The function should accept the following parameters:

- `protocol`: The protocol of the URL, either 'http' or 'https'.
- `domain`: The core domain of the URL.
- `path`: A list of path hierarchies (optional).
- `subdomain`: The subdomain of the URL (optional).
- `query_parameters`: A dictionary of query parameters (optional).
- `fragments`: The fragment identifier of the URL (optional).

The function should return a properly formatted URL string.
"""

import urllib.parse

def create_url(protocol, domain, path=None, subdomain=None, 
               query_parameters=None, fragments=None):
    n_path = ''
    if path:
        n_path = '/' + '/'.join(path)
        
    n_netloc = domain
    if subdomain:
        n_netloc = subdomain + '.' + n_netloc

    url_parts = (protocol, n_netloc, n_path, '', '', '')
    complex_url = urllib.parse.urlunparse(url_parts)
    
    if query_parameters:
        complex_url += '?' + urllib.parse.urlencode(query_parameters)
    
    if fragments:
        complex_url += '#' + fragments

    return complex_url