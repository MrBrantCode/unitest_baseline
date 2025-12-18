"""
QUESTION:
Create a function named `find_median` that takes three integers as input and returns the median value without using any built-in functions. The function should not use any sorting algorithms or built-in sorting functions, such as `sort()`, `sorted()`, or `median()`, from libraries like statistics.
"""

def find_median(a, b, c):
    """
    This function finds the median of three integers without using any built-in sorting functions.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        int: The median of the three integers.
    """
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if b < c:
            return b
        elif a > c:
            return a
        else:
            return c