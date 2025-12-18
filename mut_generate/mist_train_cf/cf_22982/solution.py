"""
QUESTION:
Write a function named `remove_odd_elements` that takes a dictionary as input, removes all key-value pairs where the value is an odd number, and returns the resulting dictionary. The function should not modify the original dictionary.
"""

def remove_odd_elements(input_dict):
    """
    This function removes all key-value pairs from a dictionary where the value is an odd number.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        dict: A new dictionary with all odd elements removed.
    """
    return {key: value for key, value in input_dict.items() if value % 2 == 0}