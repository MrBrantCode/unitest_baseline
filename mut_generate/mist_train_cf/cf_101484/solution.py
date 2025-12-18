"""
QUESTION:
Write a function named `calculate_arithmetic_series_sum` that takes two parameters: `n` (the number of terms) and `a_1` (the first term). The common difference should be 1. Calculate and return the sum of the first `n` terms of the arithmetic series using the formula `S_n = n/2 * (2*a_1 + (n-1)*d)`.
"""

def calculate_arithmetic_series_sum(n, a_1):
    """
    Calculate the sum of the first n terms of an arithmetic series.
    
    Parameters:
    n (int): The number of terms.
    a_1 (int): The first term.
    
    Returns:
    int: The sum of the first n terms of the arithmetic series.
    """
    d = 1  # The common difference is 1
    return n/2 * (2*a_1 + (n-1)*d)