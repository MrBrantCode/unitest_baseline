"""
QUESTION:
Create a URL builder function, URLBuilder, that generates a URL from given parameters and supports updating, removing, and resetting these parameters. The URL should be in the format:

    protocol://subdomain.domain.com/path;matrixParam=value/routeParam?queryParam=value#fragment

The function should accept the following parameters:
- protocol
- subdomain
- domain
- path
- matrix_params (dictionary of matrix parameters)
- route_params (dictionary of route parameters)
- query_params (dictionary of query parameters)
- fragment (fragment identifier)

The function should support the following operations:
- Adding or updating parameters (matrix, route, query)
- Removing parameters (matrix, route, query)
- Resetting the URL to its original state
- Encoding and decoding URL components

The function should validate the URL syntax and raise exceptions for non-compliance. It should also handle scenarios where parameters appear after the fragment identifier, single parameters contain multiple values, and matrix and route parameters are included in the URL construction.
"""

from urllib.parse import urlencode, urlparse, parse_qs, unquote, quote
import re

def URLBuilder(protocol, subdomain, domain, path, matrix_params={}, route_params={}, query_params={}, fragment=''):
    """
    This function generates a URL from given parameters and supports updating, removing, and resetting these parameters.
    
    Parameters:
    protocol (str): The protocol used in the URL (e.g., http, https)
    subdomain (str): The subdomain of the URL
    domain (str): The domain of the URL
    path (str): The path of the URL
    matrix_params (dict): Dictionary of matrix parameters
    route_params (dict): Dictionary of route parameters
    query_params (dict): Dictionary of query parameters
    fragment (str): The fragment identifier of the URL
    
    Returns:
    str: The generated URL
    """
    url = f"{protocol}://{subdomain}.{domain}/{quote(path)}"
    if matrix_params:
        url += ';' + urlencode(matrix_params)
    if route_params:
        url += '/' + urlencode(route_params)
    if query_params:
        url += '?' + urlencode(query_params, doseq=True)
    if fragment:
        url += '#' + fragment
    return url