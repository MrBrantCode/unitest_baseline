"""
QUESTION:
Write a function named `custom_sort_dict` that takes a dictionary as input, sorts its items in descending order based on their values while ignoring items with a value of `None`, and in case of a tie, sorts the keys in ascending order.
"""

def custom_sort_dict(my_dict):
    """
    Sorts a dictionary in descending order based on its values, ignoring items with a value of None.
    In case of a tie, sorts the keys in ascending order.

    Args:
        my_dict (dict): The input dictionary to be sorted.

    Returns:
        dict: The sorted dictionary.
    """
    return {k: v for k, v in sorted(my_dict.items(), key=lambda item: (-item[1] if item[1] is not None else float('-inf'), item[0]))}