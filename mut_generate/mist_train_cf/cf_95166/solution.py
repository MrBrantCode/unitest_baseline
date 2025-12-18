"""
QUESTION:
Develop a function called `fetch_max_value` that takes a nested dictionary as input and returns the maximum value among all the values in the dictionary. The dictionary can have multiple levels of nesting, and the values can be either a single value or a list of values. The function should handle different data types, including integers, and compare them to find the maximum value.
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