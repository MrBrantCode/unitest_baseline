"""
QUESTION:
Create a function `sort_dict_by_values` that takes a dictionary as input, where the values are expected to be numerical. The function should handle non-numerical and missing values by replacing them with 0, and return two outputs: a new dictionary sorted by the numerical values and a list of keys in the same sorted order.
"""

def sort_dict_by_values(my_dict):
    # Checking for non numeric values and/or missing values
    for key, value in my_dict.items():
        if not isinstance(value, (int, float)):
            my_dict[key] = 0 # set the value to zero if it's non-numerical or missing

    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    sorted_keys = list(sorted_dict.keys())

    return sorted_dict, sorted_keys