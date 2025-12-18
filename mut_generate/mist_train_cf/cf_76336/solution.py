"""
QUESTION:
Write a function named `filter_dict` that takes in a dictionary `dict_to_filter`, a list of keys or values `keys_or_values`, and an optional `filter_by` parameter that defaults to `'keys'`. The function should return a new dictionary with elements from the original dictionary filtered by the list of keys or values provided, depending on the `filter_by` parameter. The function should handle cases where some keys or values in the list are not present in the dictionary and vice versa, without raising errors. If the `filter_by` parameter is not provided, it should default to filtering by keys.
"""

def filter_dict(dict_to_filter, keys_or_values, filter_by='keys'):
    filtered_dict = {}
    if filter_by == 'keys':
        for key in keys_or_values:
            if key in dict_to_filter.keys():
                filtered_dict[key] = dict_to_filter[key]
    elif filter_by == 'values':
        for key, value in dict_to_filter.items():
            if value in keys_or_values:
                filtered_dict[key] = value
    else:
        print("The filter_by input is invalid.")
    return filtered_dict