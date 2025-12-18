"""
QUESTION:
Design a function `sum_of_digits(n)` that calculates the sum of the digits in the result of a factorial mathematical operation for a given input `n`. The function should return the sum of the digits of `n!`. Assume `n` is a non-negative integer. Note that the function should be able to handle factorials that do not exceed the maximum limit of an integer in Python.
"""

def sum_of_digits(n):
    """
    Calculate the sum of the digits in the result of a factorial mathematical operation for a given input n.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        int: The sum of the digits of n!.
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return sum(int(digit) for digit in str(factorial))