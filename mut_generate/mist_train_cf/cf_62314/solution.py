"""
QUESTION:
Write a function `swap_distinct_integers(a, b)` that takes two distinct integers as input and returns the swapped values of `a` and `b` without using a third variable or built-in functions. The function should not modify the original values of `a` and `b` before swapping.
"""

def swap_distinct_integers(a, b):
    """
    Swap the values of two distinct integers without using a third variable or built-in functions.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        tuple: A tuple containing the swapped values of a and b.
    """
    a = a + b  # adding both the numbers
    b = a - b  # subtract second number from the sum 
    a = a - b  # subtract the new value of second number from the sum

    return a, b