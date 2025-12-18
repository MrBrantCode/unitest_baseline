"""
QUESTION:
Write a function named `multiply_numbers` that calculates the product of two given integers without using the multiplication operator (*) or any built-in multiplication functions. The function should take two integers as input and return their product.

The integers can be positive, negative, or zero. The function should handle these cases correctly.
"""

def multiply_numbers(a, b):
    """
    Calculate the product of two given integers without using the multiplication operator (*) or any built-in multiplication functions.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.
    """
    product = 0
    if b < 0:
        for _ in range(abs(b)):
            product -= a
    else:
        for _ in range(b):
            product += a
    return product