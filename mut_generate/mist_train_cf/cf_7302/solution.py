"""
QUESTION:
Write a function `extract_query_params(url)` that takes a URL as input, checks if the URL contains a query string parameter named "food" with the value "burger" (case-insensitive), and if found, extracts and returns the values of all other query string parameters present in the URL while excluding any query string parameters that have the same name as the "food" parameter or have the same value as the "food" parameter if the parameter name is not "food".
"""

def extract_query_params(url):
    params = []
    food_value = None

    query_string = url.split('?')[1]
    query_params = query_string.split('&')

    for param in query_params:
        name, value = param.split('=')

        if name.lower() == 'food':
            food_value = value.lower()
        else:
            if food_value is not None and food_value == value.lower():
                continue
            params.append(param)

    return params