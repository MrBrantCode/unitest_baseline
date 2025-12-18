"""
QUESTION:
Write a function `sum_of_series(n)` to calculate the sum of the series 1^4 + 2^4 + 3^4 + ... + n^4. The input `n` is a positive integer, and the function should return the sum of the series from 1 to `n`. If `n` is not a positive integer, the function should return an error message.
"""

def entance(n):
    if n <= 0:
        return "Invalid input! n should be a positive integer."
    else:
        series_sum = sum([i**4 for i in range(1, n+1)])
        return series_sum