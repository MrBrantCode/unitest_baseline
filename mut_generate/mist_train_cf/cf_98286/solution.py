"""
QUESTION:
Write a function called `sort_dict_list` that takes in three arguments: a list of dictionaries `dict_list`, a string representing the key to sort by `sort_key`, and a boolean value `descending` indicating whether the sorting should be in descending order. The function should return a new list of dictionaries sorted by the values associated with the key specified in `sort_key`. If a dictionary is missing the key, it should be sorted to the bottom of the list when `descending` is `False` and to the top of the list when `descending` is `True`.
"""

def sort_dict_list(dict_list, sort_key, descending=False):
    """
    Sorts a list of dictionaries based on a specific key in each dictionary.

    Args:
        dict_list (List[Dict]): The list of dictionaries to sort.
        sort_key (str): The key in each dictionary to sort by.
        descending (bool): Whether to sort in descending order.

    Returns:
        List[Dict]: The sorted list of dictionaries.
    """
    
    # Sort the list of dictionaries based on the specified key.
    dict_list.sort(key=lambda d: d.get(sort_key, float('inf')))

    # If descending is True, reverse the order of the sorted list.
    if descending:
        dict_list.reverse()

    return dict_list