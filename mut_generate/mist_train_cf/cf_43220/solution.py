"""
QUESTION:
Create a function `parseURI` that takes a URI string as input and returns a dictionary containing its components. The dictionary should include `scheme`, `host`, `path`, `query`, and `fragment`. The `query` component should be a dictionary of key-value pairs. If a component is not present in the URI, the corresponding value in the dictionary should be an empty string or an empty dictionary.
"""

import urllib.parse

def parseURI(uri):
    parsed_uri = urllib.parse.urlparse(uri)
    query_params = urllib.parse.parse_qs(parsed_uri.query)
    
    uri_components = {
        "scheme": parsed_uri.scheme,
        "host": parsed_uri.netloc,
        "path": parsed_uri.path,
        "query": dict(query_params),
        "fragment": parsed_uri.fragment
    }
    
    return uri_components