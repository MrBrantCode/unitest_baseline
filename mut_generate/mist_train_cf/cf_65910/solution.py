"""
QUESTION:
Write a function named `count_parameters` that takes a URL as an input and returns the number of top-level and nested parameters present in the URL. The function should be able to handle both encoded and non-encoded URL formats. A nested parameter is defined as a parameter that has another parameter as a prefix to its name, indicated by a '[' character. The function should count each top-level parameter only once, even if it has nested parameters.
"""

from urllib.parse import urlparse, parse_qs, unquote

def count_parameters(url):
    url = unquote(url)
    query = urlparse(url).query
    params = parse_qs(query)
    
    top_level_count = 0
    nested_count = 0
    for param, value in params.items():
        if '[' in param:
            top_param = param.split('[')[0]
            if not any(top_param in key for key in params.keys() if key != param):
                top_level_count += 1
            nested_count += len(value)
        else:
            top_level_count += 1
    return top_level_count, nested_count