"""
QUESTION:
Create a function `parse_uri` that takes a URI string as input and returns a dictionary containing the parsed components. The function should extract the following components:
- `scheme`: the protocol or scheme used in the URI
- `username`: the username specified in the URI
- `password`: the password specified in the URI
- `host`: the host or domain name
- `port`: the port number (as an integer or None if not specified)
- `path`: the path component of the URI
- `query`: the query parameters as a dictionary (with list values if a key appears multiple times)
- `fragment`: the fragment or anchor part of the URI (as an empty string if not specified)

The function should handle cases where certain components may be missing from the URI.
"""

import urllib.parse

def parse_uri(uri):
    parsed_uri = urllib.parse.urlparse(uri)
    query_params = urllib.parse.parse_qs(parsed_uri.query)
    port = parsed_uri.port if parsed_uri.port else None
    query_dict = {key: value[0] if len(value) == 1 else value for key, value in query_params.items()}
    
    return {
        'scheme': parsed_uri.scheme,
        'username': parsed_uri.username if parsed_uri.username else '',
        'password': parsed_uri.password if parsed_uri.password else '',
        'host': parsed_uri.hostname,
        'port': port,
        'path': parsed_uri.path,
        'query': query_dict,
        'fragment': parsed_uri.fragment if parsed_uri.fragment else ''
    }