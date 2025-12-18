"""
QUESTION:
Write a function named `exponential` to compute the exponential of a given number `x` without using any built-in functions or modules related to exponentiation or mathematical calculations. The function should only use basic arithmetic operations and loops to approximate the exponential using the Taylor series expansion.
"""

def exponential(x, n=10):
    """
    Compute the exponential of x using Taylor series expansion.

    Args:
    x (float): The base number.
    n (int, optional): The number of terms in the series. Defaults to 10.

    Returns:
    float: The exponential of x.
    """
    result = 1
    for i in range(1, n+1):
        term = 1
        for j in range(1, i+1):
            term *= x
        factorial = 1
        for k in range(1, i+1):
            factorial *= k
        result += term / factorial
    return result