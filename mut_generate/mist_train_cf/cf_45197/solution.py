"""
QUESTION:
Create a function named `build_url` that constructs a URL with query parameters, given a protocol, subdomain, primary domain, resource path, and query parameters. The function should encode the query parameters into a URL-safe format and return the full URL as a string.

The input parameters for the function are:
- protocol (str)
- subdomain (str)
- primary_domain (str)
- path (str)
- params (dict)

Restrictions:
- The protocol should be in the format "https://" or "http://"
- The subdomain and primary domain should not include any protocol or path information
- The path should not include any query parameters or fragments
- The params should be a dictionary of key-value pairs to be encoded as URL query parameters

The function should return a string representing the full URL with the query parameters encoded correctly.
"""

import urllib.parse

def build_url(protocol, subdomain, primary_domain, path, params):
    """
    Construct a URL with query parameters.

    Args:
    protocol (str): The protocol of the URL (e.g., "https://", "http://").
    subdomain (str): The subdomain of the URL.
    primary_domain (str): The primary domain of the URL.
    path (str): The path of the URL.
    params (dict): A dictionary of key-value pairs to be encoded as URL query parameters.

    Returns:
    str: The full URL with the query parameters encoded correctly.
    """

    # Assemble the URL without the query parameters
    base_url = protocol + subdomain + primary_domain + path 

    # URL-encode the query parameters
    query_params = urllib.parse.urlencode(params) 

    # Construct the full URL
    full_url = base_url + "?" + query_params if query_params else base_url

    return full_url