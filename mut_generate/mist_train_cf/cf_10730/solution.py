"""
QUESTION:
Write a function `sum_of_series(n)` that calculates the sum of the series 1^3 + 2^3 + 3^3 + ... + n^3. The function should take an integer `n` as input and return the sum of the series.
"""

def sum_of_series(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i**3
    return total_sum