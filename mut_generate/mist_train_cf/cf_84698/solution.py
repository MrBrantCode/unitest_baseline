"""
QUESTION:
Write a function `find_root(value, degree)` that calculates the root of a given number `value` with a specified `degree` without using built-in root or power functions. The function should handle potential exceptions and edge cases by returning the closest possible representation of the root with a specified accuracy level. The function should be used to find and print the square, cube, and fourth roots of numbers from 1 to 20, along with an indication of whether each root is a whole number.
"""

def find_root(value, degree):
    """
    Calculate the root of a given number 'value' with a specified 'degree' without using built-in root or power functions.

    Args:
    value (float): The number for which the root needs to be calculated.
    degree (int): The degree of the root.

    Returns:
    float: The calculated root.
    """
    epsilon = 0.01
    g = value / 2.0
    while abs(g**degree - value) >= epsilon:
        g -= ((g**degree - value) / (degree * g**(degree-1)))
    return round(g, 2)