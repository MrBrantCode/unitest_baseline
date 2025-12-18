"""
QUESTION:
Write a function named `arithmetic_series_sum` that calculates the sum of the first n terms of an arithmetic series given the first term `a_1`, the common difference `d`, and the number of terms `n`. The function should return the sum of the first n terms of the arithmetic series. The function should not take any other arguments besides `a_1`, `d`, and `n`.
"""

def arithmetic_series_sum(a_1, d, n):
    return n/2 * (2*a_1 + (n-1)*d)