"""
QUESTION:
Write a function `swap_variables` that swaps the values of two variables without using a temporary variable, arithmetic operations, or built-in functions, and achieves a time complexity of O(1). The function should take two variables as input and return the swapped values.
"""

def swap_variables(a, b):
    """
    Swap the values of two variables without using a temporary variable, 
    arithmetic operations, or built-in functions.

    Args:
        a (any): The first variable.
        b (any): The second variable.

    Returns:
        tuple: A tuple containing the swapped values of a and b.
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b