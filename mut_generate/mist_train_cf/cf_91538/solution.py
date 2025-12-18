"""
QUESTION:
Create a function named `sort_list_of_dicts` that takes a list of dictionaries and three keys as arguments. The function should sort the list of dictionaries in ascending order based on the given keys. The first key should be sorted case-insensitively, the second key should be sorted in alphabetical order in descending order, and the third key should be sorted numerically in descending order if the first two keys are the same.
"""

def sort_list_of_dicts(lst, key1, key2, key3):
    """
    Sorts a list of dictionaries in ascending order based on the given keys.
    The first key is sorted case-insensitively, the second key is sorted in 
    alphabetical order in descending order, and the third key is sorted numerically 
    in descending order if the first two keys are the same.

    Args:
        lst (list): The list of dictionaries to be sorted.
        key1 (str): The first key for sorting.
        key2 (str): The second key for sorting.
        key3 (str): The third key for sorting.

    Returns:
        list: The sorted list of dictionaries.
    """

    sorted_list = sorted(lst, key=lambda x: (x[key1].lower(), x[key2], -x[key3]))
    return sorted_list