"""
QUESTION:
Create a function named `url_generator` that generates an internet address utilizing the provided details and validates it against the official URL regex. The function should take in a protocol, subdomain, domain, path, and a dictionary containing key/value pairs for each query parameter. The function should encode each query parameter value using Base64.

Additionally, create a function named `url_decoder` that takes a URL and returns the original parameters and their values after Base64 decryption.

The functions should handle multiple query parameters and implement appropriate error handling for cases where the URL is invalid or the Base64 decryption produces an error.
"""

import urllib.parse
import re
import base64

def url_generator(protocol, subdomain, domain, path, param_dict):
    """
    Generates an internet address utilizing the provided details and validates it against the official URL regex.
    The function takes in a protocol, subdomain, domain, path, and a dictionary containing key/value pairs for each query parameter.
    The function encodes each query parameter value using Base64.
    
    Args:
        protocol (str): The protocol to use (e.g., http, https).
        subdomain (str): The subdomain.
        domain (str): The domain.
        path (str): The path.
        param_dict (dict): A dictionary containing key/value pairs for each query parameter.
    
    Returns:
        str: The constructed URL.
    """
    base64_encoded_params = {}

    for key, val in param_dict.items():
        base64_encoded_params[key] = base64.b64encode(val.encode()).decode()

    encoded_query = urllib.parse.urlencode(base64_encoded_params)
    url = f"{protocol}://{subdomain}.{domain}/{path}?{encoded_query}"

    return url


def url_decoder(url):
    """
    Takes a URL and returns the original parameters and their values after Base64 decryption.
    
    Args:
        url (str): The URL to decode.
    
    Returns:
        dict: A dictionary containing the original parameters and their values.
    """
    base64_decoded_params = {}
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, url):
        query_string = urllib.parse.urlparse(url).query
        query_dict = urllib.parse.parse_qs(query_string)

        for key, val in query_dict.items():
            base64_decoded_params[key] = base64.b64decode(val[0]).decode()

        return base64_decoded_params
    else:
        return "Invalid URL"