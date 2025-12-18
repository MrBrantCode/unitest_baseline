"""
QUESTION:
Implement a function named `sort_dict_by_value_and_key` that sorts a dictionary by its values in descending order, ignoring items with a value of None. If two items have the same value, sort them by their keys in ascending order.
"""

def sort_dict_by_value_and_key(input_dict):
    """
    Sorts a dictionary by its values in descending order, ignoring items with a value of None.
    If two items have the same value, sort them by their keys in ascending order.

    Args:
        input_dict (dict): The dictionary to be sorted.

    Returns:
        dict: The sorted dictionary.
    """
    return {k: v for k, v in sorted(input_dict.items(), key=lambda item: (-item[1] if item[1] is not None else float('-inf'), item[0]))}