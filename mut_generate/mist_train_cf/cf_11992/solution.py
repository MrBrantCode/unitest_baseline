"""
QUESTION:
Create a function called swap_variables that takes two integer arguments and returns their values swapped without using a temporary variable or built-in swapping functions.
"""

def swap_variables(a, b):
    """
    Swap two integer values without using a temporary variable or built-in swapping functions.

    Args:
        a (int): The first integer to be swapped.
        b (int): The second integer to be swapped.

    Returns:
        tuple: A tuple containing the swapped values of a and b.
    """
    a = a + b
    b = a - b
    a = a - b
    return a, b