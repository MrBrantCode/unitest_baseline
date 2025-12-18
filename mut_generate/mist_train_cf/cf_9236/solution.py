"""
QUESTION:
Create a function called swap_variables that takes two variables as input and returns the swapped values without using a temporary variable. The function should work with any data type that supports the XOR operation.
"""

def swap_variables(a, b):
    """
    Swap two variables without using a temporary variable.

    This function uses the XOR operator to swap the values of two variables.
    
    Parameters:
    a (any data type that supports XOR operation): The first variable to swap.
    b (any data type that supports XOR operation): The second variable to swap.

    Returns:
    tuple: A tuple containing the swapped values of a and b.
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b