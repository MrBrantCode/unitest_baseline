"""
QUESTION:
Generate a function `generate_url` that takes in the following parameters: 
- protocol (str): the protocol of the URL (either 'https' or 'http')
- domain (str): the domain of the URL
- path (str, optional): the path of the URL
- subdomain (str, optional): the subdomain of the URL
- params (dict, optional): a dictionary of key-value pairs for query parameters

The function should return a correctly encoded and formatted URL string. If any of the optional parameters (path, subdomain, params) are not provided, they should not be included in the generated URL.
"""

from urllib import parse

def generate_url(protocol, domain, path=None, subdomain=None, params=None):
    netloc = domain
    if subdomain:
        netloc = f"{subdomain}.{domain}"
  
    scheme = protocol
    url_parts = list(parse.urlsplit(scheme + "://" + netloc))
    if path:
        url_parts[2] = path    # Set path.

    if params:  
        url_parts[4] = parse.urlencode(params)    # Set query.

    # Combines the URL components into a URL string.
    url = parse.urlunsplit(url_parts)
    return url