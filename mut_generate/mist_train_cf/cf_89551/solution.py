"""
QUESTION:
Write a function named `swap_values` that swaps the values of two variables 'a' and 'b' without using a temporary variable, any mathematical operations (+, -, *, /), or any bitwise operators (&, |, ^, <<, >>). The function should take two arguments, 'a' and 'b', and return the swapped values.
"""

def swap_values(a, b):
    """
    Swap the values of two variables 'a' and 'b' without using a temporary variable, 
    any mathematical operations (+, -, *, /), or any bitwise operators (&, |, ^, <<, >>).
    
    Args:
    a (any): The first variable to be swapped.
    b (any): The second variable to be swapped.
    
    Returns:
    tuple: A tuple containing the swapped values of 'a' and 'b'.
    """
    a, b = b, a  # Swap the values of 'a' and 'b' using tuple packing and unpacking.
    return a, b