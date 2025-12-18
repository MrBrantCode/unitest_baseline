"""
QUESTION:
Add two integers using only bitwise operators without the "+" operator.

Write a function `add(x, y)` that takes two integers as input and returns their sum. The function should not use any type conversion or the "+" operator, but instead utilize bitwise operators to perform the addition.
"""

def add(x, y):
    """
    Add two integers using only bitwise operators without the "+" operator.

    Args:
        x (int): The first integer to add.
        y (int): The second integer to add.

    Returns:
        int: The sum of x and y.
    """
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x