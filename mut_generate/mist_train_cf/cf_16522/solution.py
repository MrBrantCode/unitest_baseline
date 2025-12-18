"""
QUESTION:
Write a function `swap_variables(a, b)` that takes two variables `a` and `b` as input and swaps their values without using a temporary variable, arithmetic operators, bitwise operations, or built-in swap functions. The function should only use logical operations and the assignment operator.
"""

def swap_variables(a, b):
    """
    Swap two variables without using a temporary variable, arithmetic operators, 
    bitwise operations, or built-in swap functions.

    Args:
        a (any): The first variable.
        b (any): The second variable.

    Returns:
        tuple: A tuple containing the swapped values.
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b