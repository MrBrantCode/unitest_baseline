"""
QUESTION:
Create a function named `lowest_common_multiple(x, y)` that takes two positive integers `x` and `y` as input and returns their lowest common multiple. The function should handle all possible positive integer inputs and return the smallest number that is a multiple of both `x` and `y`.
"""

def lowest_common_multiple(x, y):
    """
    This function calculates the lowest common multiple of two positive integers x and y.

    Parameters:
    x (int): The first positive integer.
    y (int): The second positive integer.

    Returns:
    int: The lowest common multiple of x and y.
    """
    maximum = max(x, y)
    lcm = maximum
    
    while True:
        if lcm % x == 0 and lcm % y == 0:
            return lcm
        else:
            lcm += maximum