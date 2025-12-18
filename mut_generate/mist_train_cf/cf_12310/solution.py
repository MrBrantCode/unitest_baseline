"""
QUESTION:
Write a function `sum_nested_dictionary` that calculates the sum of all values in a nested dictionary. The function should recursively traverse the dictionary and add up all values, regardless of their nesting level. The input dictionary can have an arbitrary number of levels and may contain both numeric and dictionary values. If a value is a dictionary, the function should recursively call itself on that dictionary; if the value is not a dictionary, it should be added to the total sum.
"""

def sum_nested_dictionary(dictionary):
    """
    This function calculates the sum of all values in a nested dictionary.
    
    Args:
        dictionary (dict): The dictionary to calculate the sum from.
    
    Returns:
        int: The sum of all values in the dictionary.
    """
    total = 0
    for key, value in dictionary.items():
        if isinstance(value, dict):
            total += sum_nested_dictionary(value)
        else:
            total += value
    return total