"""
QUESTION:
Write a function called `swap_variables` that swaps the values of two input variables without using any arithmetic or assignment operators.
"""

def swap_variables(a, b):
    """
    Swap the values of two input variables without using any arithmetic or assignment operators.

    Args:
        a (int): The first variable.
        b (int): The second variable.

    Returns:
        tuple: A tuple containing the swapped values.
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b