"""
QUESTION:
Write a function `swap_variables(a, b)` that swaps the values of two variables `a` and `b` without using a temporary variable and only using a maximum of 2 assignment statements. The function should return the swapped values of `a` and `b`.
"""

def swap_variables(a, b):
    """
    Swaps the values of two variables a and b without using a temporary variable.
    
    Args:
        a (any): The first variable to swap.
        b (any): The second variable to swap.
    
    Returns:
        tuple: A tuple containing the swapped values of a and b.
    """
    a = a + b
    b = a - b
    a = a - b
    return a, b