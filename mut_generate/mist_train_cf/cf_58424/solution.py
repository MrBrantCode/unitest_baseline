"""
QUESTION:
Create a function `brazilian_factorial(n)` that calculates the product of factorials from `n!` down to `1!`, where `n` is a positive integer. The function should take an integer `n` as input and return the result of the calculation.
"""

def brazilian_factorial(n):
    """
    Calculate the product of factorials from n! down to 1!.

    Args:
        n (int): A positive integer.

    Returns:
        int: The product of factorials from n! down to 1!.
    """
    result = 1
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        result *= fact
    return result