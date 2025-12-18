"""
QUESTION:
Implement a function named `build` that constructs a URL from its components, including protocol, subdomain, main domain, path, matrix parameters, route parameters, query parameters, and fragment. The function should be able to handle an arbitrary number of parameters, encode and decode URL components, and validate the resulting URL. 

The function should be able to modify or remove existing parameters and revert the URL to its original state. It should also handle advanced scenarios such as multiple values for a single parameter, matrix and route parameters, and parameters after a fragment identifier.

The input parameters for the function are: 

- scheme (string): the protocol of the URL
- netloc (string): the subdomain and main domain of the URL
- path (string): the path of the URL
- params (dictionary): the matrix parameters of the URL
- query (dictionary): the query parameters of the URL
- fragment (string): the fragment of the URL

The function should return the constructed URL as a string. If the input parameters are invalid, the function should raise an exception.
"""

from urllib.parse import urlunparse, urlencode

def build(scheme, netloc, path, params, query, fragment):
    """
    Construct a URL from its components.

    Args:
    - scheme (string): the protocol of the URL
    - netloc (string): the subdomain and main domain of the URL
    - path (string): the path of the URL
    - params (dictionary): the matrix parameters of the URL
    - query (dictionary): the query parameters of the URL
    - fragment (string): the fragment of the URL

    Returns:
    - string: the constructed URL
    """
    # Construct the path with matrix parameters
    path_with_params = f'{path};{";".join([f"{k}={v}" for k,v in params.items()])}' if params else path
    
    # Encode query parameters
    encoded_query = urlencode(query, doseq=True)
    
    # Construct the URL
    url = urlunparse((scheme, netloc, path_with_params, '', encoded_query, fragment))
    
    return url