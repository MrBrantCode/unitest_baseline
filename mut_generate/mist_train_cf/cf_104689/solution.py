"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given number `n`. The function should return the product of all positive integers less than or equal to `n` for non-negative `n`, and an error message for negative `n`. Note that `n` can be a large number, and the function should handle the case where `n` is zero.
"""

def factorial(n):
    """
    Calculate the factorial of a given number n.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The product of all positive integers less than or equal to n.
    str: An error message if n is negative.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result