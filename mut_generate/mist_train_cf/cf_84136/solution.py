"""
QUESTION:
Write a function named `sort_dict_of_dicts` that takes two parameters: a dictionary of dictionaries `d` and a function `key_func`. The function should sort the dictionary `d` based on the values returned by applying `key_func` to the inner dictionaries and return the sorted dictionary in descending order. The `key_func` can be any function, including lambda functions, that takes an inner dictionary as input and returns a value that can be used for sorting.
"""

def sort_dict_of_dicts(d, key_func):
    """
    Function to sort a dictionary of dictionaries
    as per a given function.
    :param d: Dictionary to be sorted.
    :param key_func: Function used for sorting.
    :Returns : Sorted dictionary.
    """
    return dict(sorted(d.items(), key=lambda x: key_func(x[1]), reverse=True))