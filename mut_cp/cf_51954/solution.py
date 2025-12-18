"""
ORIGINAL QUESTION:
Create a function called `sort_nested_dict` that takes a nested dictionary as input. The function should sort the inner dictionaries by their values in ascending order, and in case of a tie, sort by the keys in lexicographical order. The function should handle both integers and floating point numbers. The outer dictionary keys should also be sorted in ascending lexicographical order.
"""

def sort_nested_dict(nested_dict):
    """
    Sorts the inner dictionaries by their values in ascending order, 
    and in case of a tie, sort by the keys in lexicographical order.
    The outer dictionary keys are also sorted in ascending lexicographical order.

    Args:
        nested_dict (dict): A dictionary containing inner dictionaries.

    Returns:
        dict: A new nested dictionary with sorted inner dictionaries.
    """
    # Sort the outer dictionary keys
    sorted_dict = {key : nested_dict[key] for key in sorted(nested_dict)}

    # Sort inner dictionaries by value and if tie occurs then by key
    for key, inner_dict in sorted_dict.items():
        sorted_dict[key] = dict(sorted(inner_dict.items(), key=lambda item: (item[1], item[0])))

    return sorted_dict