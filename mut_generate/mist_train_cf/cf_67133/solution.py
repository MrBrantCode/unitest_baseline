"""
QUESTION:
Create a function called `create_url` that generates an HTTP request URL. The function should accept the following parameters: `protocol`, `subdomain`, `domain`, `path`, and `parameters`. The `protocol` parameter should be either 'http' or 'https'. The `parameters` parameter should be a dictionary. The function should handle URL encoding to make the URL RFC 3986 compliant and correctly represent Unicode characters. The function should also include error handling to inform users about incorrectly formatted input parameters.
"""

from urllib.parse import urlencode, quote, urlunparse

def create_url(protocol, subdomain, domain, path, parameters):
    """
    Generate an HTTP request URL.

    Args:
        protocol (str): The protocol to use, either 'http' or 'https'.
        subdomain (str): The subdomain of the URL.
        domain (str): The domain of the URL.
        path (str): The path of the URL.
        parameters (dict): The parameters to be included in the URL.

    Returns:
        str: The constructed URL.

    Raises:
        Exception: If the protocol is not 'http' or 'https', or if the parameters are not in dictionary format.
    """
    try:
        # Check if the protocol is in http or https, if not raise an exception
        if protocol not in ("http", "https"):
            raise Exception("Invalid protocol. Please enter either 'http' or 'https' ")
        
        # Check if subdomain, domain and path are string values
        for item in [subdomain, domain, path]:
            if not isinstance(item, str):
                raise Exception(f"Invalid {item}. Please enter a string value.")
        
        # Check if parameters is a dictionary
        if not isinstance(parameters, dict):
            raise Exception("Invalid paramters. Please enter in dictionary format.")
        
        # The netloc is combined from subdomain and domain
        netloc = f"{subdomain}.{domain}"
        
        # The parameters are url encoded to make sure that they are safe to be in a url
        query = urlencode(parameters, quote_via=quote)
        
        # urlunparse is used to construct the url from the components
        url = urlunparse((protocol, netloc, path, None, query, None))
        
        return url
        
    except Exception as e:
        raise Exception(str(e))