"""
QUESTION:
Implement a function `leibniz(n)` that takes an integer `n` as input and returns a tuple containing the approximation of π using the first `n` terms of the Leibniz series and a list of partial sums up to the nth term. The Leibniz series is defined as π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ..., and the function should use this series to calculate the approximation.
"""

def leibniz(n):
    """
    Approximates π using the first n terms of the Leibniz series.

    Args:
        n (int): The number of terms to use in the approximation.

    Returns:
        tuple: A tuple containing the approximation of π and a list of partial sums up to the nth term.
    """
    approximation = 0
    partial_sums = []
    for i in range(n):
        approximation += ((-1) ** i) * (4 / (2 * i + 1))
        partial_sums.append(approximation)
    return approximation, partial_sums