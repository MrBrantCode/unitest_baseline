"""
QUESTION:
Extract all values from a dictionary that are greater than 5 and less than 9, and return them in ascending order. Create a function named `extract_and_sort_values` that takes a dictionary as input and returns a list of values meeting the specified conditions.
"""

def extract_and_sort_values(dictionary):
    """
    Extract values from a dictionary that are greater than 5 and less than 9, 
    and return them in ascending order.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        list: A list of values meeting the specified conditions, sorted in ascending order.
    """
    return sorted([value for value in dictionary.values() if 5 < value < 9])