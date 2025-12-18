"""
QUESTION:
Create a function `optimized_function(n)` that calculates the sum of the first `n` numbers using the formula for the sum of an arithmetic progression. The function should take an optional integer `n` as input, defaulting to 1000000 if not provided. The function should return the calculated sum.

Restrictions: The function should be optimized for efficiency and its time complexity should be calculable. Unit tests should be implemented to validate the function's performance and confirm its expected behavior.
"""

def optimized_function(n=1000000):
    # formula for the sum of the first n numbers
    return n * (n + 1) // 2