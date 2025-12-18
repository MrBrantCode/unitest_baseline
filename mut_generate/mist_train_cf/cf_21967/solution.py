"""
QUESTION:
Design a function named `parse_url` that takes a URL as input and returns its components as a dictionary. The function should handle URL encoding and decoding, support parsing URLs with multiple query parameters, and handle query parameters with arrays or objects as values. The dictionary should have keys for the scheme, host, path, query parameters, and fragment identifier. The function should also validate the URL format and throw an error if it is not a valid URL.
"""

from urllib.parse import unquote, parse_qs, urlparse

def parse_url(url):
    components = {}

    # Parse URL using urlparse
    parsed_url = urlparse(url)

    # Extract scheme
    components["scheme"] = parsed_url.scheme

    # Extract host
    components["host"] = parsed_url.netloc

    # Extract path
    components["path"] = parsed_url.path

    # Extract fragment identifier
    components["fragment"] = parsed_url.fragment

    # Decode and parse query parameters
    query_string = parsed_url.query
    query_params = parse_qs(query_string)

    # Decode query parameter keys and values
    decoded_query_params = {}
    for key, values in query_params.items():
        decoded_key = unquote(key)
        decoded_values = [unquote(value) for value in values]
        decoded_query_params[decoded_key] = decoded_values

    # Assign decoded query parameters to components
    components["query_parameters"] = decoded_query_params

    return components