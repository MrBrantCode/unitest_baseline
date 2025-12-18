"""
QUESTION:
Implement the `sign` function that generates a signed query string by adding a signature to the original URL parameters. The function should take a client key and a dictionary of URL parameters as input, sort the parameters, generate a signature by hashing the concatenation of the client key and the sorted query string parameters using SHA-256, and append the signature to the query string. The sorted query string parameters should be in the format `key1=value1&key2=value2...` and should not include the signature parameter. The function should return the signed query string.
"""

import hashlib
from urllib.parse import urlencode

def sign(client_key, params):
    """
    Generates a signed query string by adding a signature to the original URL parameters.

    Args:
    - client_key (str): The client key used for signing.
    - params (dict): A dictionary of URL parameters.

    Returns:
    - str: The signed query string.
    """
    sorted_params = sorted(params.items(), key=lambda x: x[0])
    query_string = urlencode(sorted_params)
    signature = hashlib.sha256((client_key + query_string).encode()).hexdigest()
    signed_query_string = query_string + "&signature=" + signature
    return signed_query_string