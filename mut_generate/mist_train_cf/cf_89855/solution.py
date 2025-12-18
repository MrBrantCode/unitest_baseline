"""
QUESTION:
Write a function named `extract_query_params` that takes a URL string as input. The function should return a list of query string parameters if the URL contains a query string parameter named "food" with the value "burger" case-insensitively. The function should exclude any query string parameters that have the same name as the "food" parameter or the same value as the "food" parameter if the "food" parameter exists. The function should return an empty list if the "food" parameter does not exist or its value is not "burger" (case-insensitive). The order of the extracted query string parameters does not matter.
"""

def extract_query_params(url):
    params = []
    food_value = None

    # Extract the query string from the URL
    query_string = url.split('?')[1]

    # Split the query string into individual parameters
    query_params = query_string.split('&')

    # Iterate over each query parameter
    for param in query_params:
        # Split the parameter into name and value
        name, value = param.split('=')

        # Check if the parameter name is 'food' (case-insensitive)
        if name.lower() == 'food':
            # Store the value of the 'food' parameter
            food_value = value.lower()
        else:
            # Exclude any parameters with the same name as 'food' and append the rest to the list
            if food_value is not None and food_value == value.lower():
                continue
            params.append(param)

    # Return an empty list if the "food" parameter does not exist or its value is not "burger" (case-insensitive)
    return params if food_value == 'burger' else []