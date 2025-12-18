"""
QUESTION:
Write a function `add_query_param_to_url(url, param_name, param_value)` that takes a URL, a parameter name, and a parameter value, and returns a new URL string with the parameter added as a query string. If the original URL already contains query parameters, the new parameter should be appended with an ampersand (`&`), otherwise, it should be appended with a question mark (`?`). Assume the input URL is well-formed.
"""

def add_query_param_to_url(url, param_name, param_value):
    if '?' in url:
        return f"{url}&{param_name}={param_value}"
    else:
        return f"{url}?{param_name}={param_value}"