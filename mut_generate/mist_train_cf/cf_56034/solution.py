"""
QUESTION:
Create a function named `max_min_diff` that takes a dictionary as an argument and returns the difference between the maximum and minimum values in the dictionary. The function should be able to handle dictionaries with numeric values.
"""

def max_min_diff(d):
    """
    This function calculates the difference between the maximum and minimum values in a dictionary.
    
    Args:
        d (dict): A dictionary containing numeric values.
    
    Returns:
        int: The difference between the maximum and minimum values in the dictionary.
    """
    values = d.values()
    return max(values) - min(values)