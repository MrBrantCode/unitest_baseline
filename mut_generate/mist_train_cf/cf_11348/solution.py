"""
QUESTION:
Write a function `sum_nested_dictionary` that calculates the sum of all integer values in a nested dictionary. The dictionary can contain integers, lists of integers, and other dictionaries as values. The function should recursively traverse the dictionary and sum up all the integer values, including those inside lists and nested dictionaries.
"""

def sum_nested_dictionary(dictionary):
    """
    This function calculates the sum of all integer values in a nested dictionary.
    
    Args:
    dictionary (dict): A dictionary containing integers, lists of integers, and other dictionaries as values.
    
    Returns:
    int: The sum of all integer values in the dictionary.
    """
    total_sum = 0
    for key, value in dictionary.items():
        if isinstance(value, int):
            total_sum += value
        elif isinstance(value, list):
            total_sum += sum(value)
        elif isinstance(value, dict):
            total_sum += sum_nested_dictionary(value)
    return total_sum