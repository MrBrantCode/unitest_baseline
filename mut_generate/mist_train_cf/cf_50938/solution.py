"""
QUESTION:
Write a function `find_apex_nadir` that takes a list of numbers as input and returns the maximum (apex) and minimum (nadir) values from the list. The function should work efficiently for large lists. Note that the input list will only contain numerical values.
"""

def find_apex_nadir(numbers):
    """
    This function finds the maximum (apex) and minimum (nadir) values in a list of numbers.
    
    Parameters:
    numbers (list): A list of numerical values.
    
    Returns:
    tuple: A tuple containing the maximum and minimum values in the list.
    """
    return (max(numbers), min(numbers))