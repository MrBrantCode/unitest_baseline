"""
QUESTION:
Write a function `convert_to_floats` that takes a string of space-separated floating-point numbers as input and returns a list of floats in the same order. The function should accurately represent the decimal values.
"""

def convert_to_floats(s):
    """
    Converts a string of space-separated floating-point numbers into a list of floats.
    
    Args:
        s (str): A string of space-separated floating-point numbers.
    
    Returns:
        list: A list of floats in the same order as the input string.
    """
    return [float(i) for i in s.split()]