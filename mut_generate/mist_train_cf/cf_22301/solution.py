"""
QUESTION:
Write a function `calculate_series_sum(n)` that calculates the sum of the first n terms of the mathematical series x = 2^n / (n!), where n is a positive integer greater than 1. 

The function should validate the input to ensure it meets the requirements. If the input is invalid, the function should return an error message. The function should also be able to handle large values of n without causing overflow or memory issues and optimize the calculation of the series.
"""

import math

def calculate_series_sum(n):
    # Validate input
    if not isinstance(n, int) or n <= 1:
        return "Invalid input. n must be a positive integer greater than 1."
    
    # Calculate sum
    series_sum = 0
    
    for i in range(2, n+1):
        series_sum += 2**i / math.factorial(i)
    
    return series_sum