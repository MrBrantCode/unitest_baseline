"""
QUESTION:
Create a function named `fetch_max_value` that takes a dictionary as input and returns the maximum value among all the values in the nested dictionary. The function should be able to handle dictionaries with multiple levels of nesting and values that can be either a single value or a list of values. The function should return the maximum value found in the dictionary.
"""

def fetch_max_value(dictionary):
    max_value = None

    for value in dictionary.values():
        if isinstance(value, dict):
            nested_max = fetch_max_value(value)
            if nested_max is not None:
                if max_value is None or nested_max > max_value:
                    max_value = nested_max
        elif isinstance(value, list):
            for nested_value in value:
                if max_value is None or nested_value > max_value:
                    max_value = nested_value
        else:
            if max_value is None or value > max_value:
                max_value = value

    return max_value