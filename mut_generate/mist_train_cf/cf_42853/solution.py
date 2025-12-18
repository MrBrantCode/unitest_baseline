"""
QUESTION:
Implement the `add_query_param` function that takes a request object, a string `param_name`, and a string `param_value` as input. The function should add a query parameter with the given name and value to the URL of the request without double-escaping non-Latin characters present in the query string, and return the modified URL.
"""

from urllib.parse import urlencode, urlparse, parse_qs

def add_query_param(request, param_name, param_value):
    original_url = request.build_absolute_uri()
    parsed_url = urlparse(original_url)
    query_params = parse_qs(parsed_url.query)
    query_params[param_name] = param_value
    encoded_query = urlencode(query_params, doseq=True, safe=':/')
    modified_url = parsed_url._replace(query=encoded_query).geturl()
    return modified_url