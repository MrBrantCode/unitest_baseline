"""
QUESTION:
Write a function named multiply(a, b) that takes two integers a and b as input parameters and returns their product. The function must use a loop to calculate the product.
"""

def multiply(a, b):
    """
    Calculate the product of two integers a and b using a loop.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.
    """
    result = 0
    for _ in range(abs(b)):
        result += abs(a)
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return result
    else:
        return -result