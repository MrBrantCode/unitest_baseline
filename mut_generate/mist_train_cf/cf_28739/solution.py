"""
QUESTION:
Write a function `parse_url_params(url_path: str) -> dict` that takes a URL path as input and returns a dictionary containing the extracted parameters and their values, where the parameters are enclosed within curly braces `{}` and are in the format `key=value`. The function should handle any number of parameters, alphanumeric characters and spaces in parameter keys and values, and separate parameter keys and values by an equal sign `=`.
"""

def entrance(url_path: str) -> dict:
    params = {}
    start = url_path.find('{')
    while start != -1:
        end = url_path.find('}', start)
        if end == -1:
            break
        param_str = url_path[start + 1:end]
        key, value = param_str.split('=')
        params[key] = value
        start = url_path.find('{', end)
    return params