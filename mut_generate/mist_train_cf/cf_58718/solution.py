"""
QUESTION:
Write a function called `binomial_coefficient` that calculates the binomial coefficient of two given integers `n` and `k`, where `n` and `k` are both positive integers and `k` is less than or equal to `n`. The function should use the formula $\dbinom{n}{k} = \frac{n!}{k!(n-k)!}$ to calculate the result. Do not use any built-in functions for calculating the factorial or the binomial coefficient.
"""

def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient of two given integers n and k.

    Args:
    n (int): A positive integer.
    k (int): A positive integer less than or equal to n.

    Returns:
    int: The binomial coefficient of n and k.
    """

    # Initialize the factorial of n, k, and n-k
    n_factorial = 1
    k_factorial = 1
    n_k_factorial = 1

    # Calculate the factorial of n
    for i in range(1, n + 1):
        n_factorial *= i

    # Calculate the factorial of k
    for i in range(1, k + 1):
        k_factorial *= i

    # Calculate the factorial of n-k
    for i in range(1, n - k + 1):
        n_k_factorial *= i

    # Calculate the binomial coefficient using the formula
    result = n_factorial // (k_factorial * n_k_factorial)

    return result