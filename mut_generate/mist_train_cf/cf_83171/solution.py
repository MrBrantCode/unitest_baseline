"""
QUESTION:
Write a function `find_maximum_even_divisible(x, y, z)` that takes three integers `x`, `y`, and `z` and returns the largest even integer in the inclusive range of `[x, y]` that is evenly divisible by `z`. If no such integer exists, return -1. The function must handle invalid inputs, including negative integers and non-integers.
"""

def find_maximum_even_divisible(x, y, z):
    """
    Returns the largest even integer in the inclusive range of [x, y] that is evenly divisible by z.
    If no such integer exists or if inputs are invalid, returns -1.

    Args:
        x (int): The start of the range (inclusive).
        y (int): The end of the range (inclusive).
        z (int): The divisor.

    Returns:
        int: The largest even integer divisible by z, or -1 if no such integer exists or if inputs are invalid.
    """
    # Correctly handle negative inputs and fractions
    if x < 0 or y <= 0 or z <= 0 or not (x % 1 == 0 and y % 1 == 0 and z % 1 == 0):
        return -1
    # If x and y input out of order, swap them
    if x > y:
        x, y = y, x
    # Step down from the largest possible value, y, and test each even number for divisibility
    for i in range(y, x-1, -1):
        if i % 2 == 0 and i % z == 0:
            return i
    # If no solutions found, return -1
    return -1