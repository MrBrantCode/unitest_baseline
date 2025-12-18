"""
QUESTION:
Create a function named `sum_of_series` that takes a single positive integer parameter `n` and returns the sum of the series 1^4 + 2^4 + 3^4 + ... + n^4. The input `n` should be a positive integer greater than 0, but the function should be able to handle any positive integer.
"""

def sum_of_series(n):
    if n <= 0:
        return "Invalid input! n should be a positive integer."
    else:
        return sum([i**4 for i in range(1, n+1)])