"""
QUESTION:
Write a function named `calculate_series_sum` that calculates the sum of the first n terms of the mathematical series 1 + 2 + 3 + ... + n. The input `n` must be a positive integer greater than 1. If `n` is not valid, the function should return an error message. The function should be able to handle large values of `n` without causing overflow or memory issues.
"""

def calculate_series_sum(n):
    # Validate input
    if not isinstance(n, int) or n <= 1:
        return "Error: n must be a positive integer greater than 1."

    # Optimize the calculation
    sum_of_series = (n * (n + 1)) // 2

    return sum_of_series