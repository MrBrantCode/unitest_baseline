"""
QUESTION:
Write a function `calculate_factorial(n)` that calculates the factorial of a given number `n`. The function should be able to handle large inputs, such as `n` up to 1000, without causing a stack overflow error. The function should return the calculated factorial of `n`.
"""

def calculate_factorial(n):
    """
    Calculate the factorial of a given number n.

    Args:
        n (int): The number for which the factorial is to be calculated.

    Returns:
        int: The calculated factorial of n.
    """
    factorial = 1

    for i in range(1, n+1):
        factorial *= i

    return factorial