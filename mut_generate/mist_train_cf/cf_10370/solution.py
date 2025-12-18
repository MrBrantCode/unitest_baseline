"""
QUESTION:
Write a function named `calculateSum` that takes two positive integers as input and returns their sum without using the addition operator (+) or any other arithmetic operators, and without using built-in functions or external libraries. The function should use recursion.
"""

def calculateSum(x, y):
    """
    Calculate the sum of two numbers without using the addition operator.
    
    Args:
    x (int): The first number.
    y (int): The second number.
    
    Returns:
    int: The sum of x and y.
    """
    if y == 0:
        return x
    else:
        return calculateSum(x ^ y, (x & y) << 1)