"""
QUESTION:
Create a function `build_url` that generates an HTTP request URL with support for custom protocol, subdomain, domain, path, query parameters (in list, nested dictionary, or dictionary format), and fragment identifiers. The function should also allow for username/password HTTP authentication and support for both RFC 3986 and RFC 1738 encoding schemes. 

The function should take the following parameters:
- protocol: The protocol of the URL (e.g., https)
- username: The username for HTTP authentication
- password: The password for HTTP authentication
- subdomain: The subdomain of the URL
- domain: The domain of the URL
- path: The path of the URL
- params: The query parameters of the URL (in dictionary format)
- fragment: The fragment identifier of the URL
- rfc1738: A boolean indicating whether to use RFC 1738 encoding scheme (default is False, which uses RFC 3986 encoding scheme)

The function should return the generated URL as a string. It should also handle and represent characters from Unicode and other language character sets correctly, and raise an error for incorrectly formatted input parameters, including invalid Unicode and non-ASCII characters.
"""

from urllib.parse import urlencode, quote_plus, quote, urlparse, urlunparse

def build_url(protocol, username=None, password=None, subdomain=None, domain=None, path=None, params=None, fragment=None, rfc1738=False):
    """
    Generates an HTTP request URL with support for custom protocol, subdomain, domain, path, 
    query parameters, and fragment identifiers. The function also allows for username/password 
    HTTP authentication and supports both RFC 3986 and RFC 1738 encoding schemes.

    Args:
    - protocol (str): The protocol of the URL (e.g., https)
    - username (str): The username for HTTP authentication (default is None)
    - password (str): The password for HTTP authentication (default is None)
    - subdomain (str): The subdomain of the URL (default is None)
    - domain (str): The domain of the URL (default is None)
    - path (str): The path of the URL (default is None)
    - params (dict): The query parameters of the URL (default is None)
    - fragment (str): The fragment identifier of the URL (default is None)
    - rfc1738 (bool): A boolean indicating whether to use RFC 1738 encoding scheme (default is False, which uses RFC 3986 encoding scheme)

    Returns:
    - str: The generated URL as a string
    """

    encoded_params = {}

    # encode parameters
    if params is not None:
        for key, value in params.items():
            key = quote_plus(key) if rfc1738 else quote(key)
            value = quote_plus(value) if rfc1738 else quote(value)
            encoded_params[key] = value

    netloc = f'{subdomain}.{domain}' if subdomain else domain

    if username is not None and password is not None:
        netloc = f'{username}:{password}@{netloc}'

    url = urlunparse((
        protocol, # scheme
        netloc, # netloc
        path or '', # path
        '', # params
        urlencode(encoded_params, doseq=True), # query string
        fragment or '' # fragment
    ))

    return url