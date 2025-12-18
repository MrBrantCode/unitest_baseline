"""
QUESTION:
Construct a function `build_url` that constructs a comprehensive URL from the given protocol, subdomain, domain, path, and query parameters, handling both secure (https) and non-secure (http) protocols, multiple subdomains, varied domains, and several paths. The function should also append the specified query parameters in a structured and properly encoded way according to the RFC1738 and RFC3986 Uniform Resource Locators (URL) specification.

The function should take the following parameters:
- `protocol`: either 'https' or 'http'
- `subdomain`: any allowed string or an empty string
- `domain`: any valid domain
- `path`: any valid path or an empty string
- `query_params`: a dictionary of key-value pairs

The function should handle each component separately, predict the kind of URL based on the different combinations of the components, handle unexpected inputs, exclude non-mandatory components that are not provided, and handle special characters correctly according to the URL specifications. The implementation should have efficient time complexity and reasonable space complexity.
"""

from urllib.parse import urlencode, quote

def build_url(protocol, subdomain, domain, path, query_params):
    """
    Construct a comprehensive URL from the given protocol, subdomain, domain, path, and query parameters.

    Args:
    - protocol (str): either 'https' or 'http'
    - subdomain (str): any allowed string or an empty string
    - domain (str): any valid domain
    - path (str or list): any valid path or an empty string
    - query_params (dict): a dictionary of key-value pairs

    Returns:
    - str: A comprehensive URL
    """
    
    url = protocol + "://"
    if subdomain:
        url += subdomain + "."
    url += domain
    if path:
        if isinstance(path, list):
            url += "/" + "/".join([quote(p, safe='') for p in path])
        else:
            url += "/" + quote(path, safe='')
    if query_params:
        url += "?" + urlencode(query_params)
    return url