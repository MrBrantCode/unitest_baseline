"""
QUESTION:
Write a function named `double_values_sorted_keys` that takes a dictionary as input, sorts its keys in descending order, and returns the doubled values corresponding to the sorted keys.
"""

def double_values_sorted_keys(dictionary):
    """
    This function takes a dictionary as input, sorts its keys in descending order, 
    and returns the doubled values corresponding to the sorted keys.

    Args:
        dictionary (dict): Input dictionary

    Returns:
        list: A list of doubled values corresponding to the sorted keys
    """
    sorted_items = sorted(dictionary.items(), key=lambda x: x[0], reverse=True)
    return [value * 2 for key, value in sorted_items]