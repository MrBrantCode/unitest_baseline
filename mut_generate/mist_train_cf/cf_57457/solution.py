"""
QUESTION:
Write a function called `swap` that takes two integers as input and returns the swapped values. The function should be efficient in terms of execution speed. Consider the trade-offs between code readability, compiler optimization, CPU architecture, and potential for bugs when implementing the function. The function should not modify the original input values.
"""

def swap(a, b):
    """
    Swap two integers without modifying the original input values.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    tuple: A tuple containing the swapped values.
    """
    return b, a