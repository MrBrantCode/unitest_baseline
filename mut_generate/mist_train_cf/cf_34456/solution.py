"""
QUESTION:
Create a function called `factorial` that calculates the factorial of a given positive integer `n`. The function should take an optional argument `n` with a default value of 5. It should return the factorial of `n`, which is the product of all positive integers less than or equal to `n`.
"""

def factorial(n=5):
    """
    Calculate the factorial of a given positive integer.

    Args:
    n: An optional integer for which the factorial needs to be calculated (default is 5).

    Returns:
    The factorial of the input integer n.
    """
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f