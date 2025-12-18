"""
QUESTION:
Write a function named `sort_dict_by_value` that takes a dictionary as input, sorts it by its values in ascending order, and only includes values that are divisible by 3. The function should return the resulting dictionary.
"""

def sort_dict_by_value(dictionary):
    """
    Sorts a dictionary by its values in ascending order and only includes values that are divisible by 3.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: The resulting dictionary.
    """
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1]) if v % 3 == 0}