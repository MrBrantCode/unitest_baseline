"""
QUESTION:
Create a function named "parse_urls" which takes a single string parameter representing a URL and returns a dictionary of queries from the URL. The function should correctly parse the URL and handle multiple query parameters, nested query parameters, and query parameters with multiple values. If a query parameter appears multiple times in the URL, only the last occurrence should be included in the dictionary. Nested query parameters are represented by using square brackets ("[]") in the key and can have multiple values, which should be stored in a list.
"""

import urllib.parse

def parse_urls(url):
    parsed_url = urllib.parse.urlparse(url)
    query_string = parsed_url.query
    query_parameters = urllib.parse.parse_qs(query_string)

    parsed_parameters = {}
    for key, value in query_parameters.items():
        if "[" in key:
            nested_keys = key.split("[")
            current_dict = parsed_parameters
            for nested_key in nested_keys[:-1]:
                nested_key = nested_key.rstrip("]")
                if nested_key not in current_dict:
                    current_dict[nested_key] = {}
                current_dict = current_dict[nested_key]
            current_key = nested_keys[-1].rstrip("]")
            if current_key in current_dict:
                if not isinstance(current_dict[current_key], list):
                    current_dict[current_key] = [current_dict[current_key]]
                current_dict[current_key].append(value[0])
            else:
                current_dict[current_key] = value[0]
        else:
            parsed_parameters[key] = value[-1]

    return parsed_parameters