"""
QUESTION:
Write a function `swap_variables` that takes two integers as input and returns the swapped values without using arithmetic or assignment operators, conditional statements, or loops.
"""

def swap_variables(a, b):
    """
    Swap two integers without using arithmetic or assignment operators, 
    conditional statements, or loops.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        tuple: A tuple containing the swapped values of a and b.
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b