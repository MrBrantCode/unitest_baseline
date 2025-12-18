"""
QUESTION:
Write a function `sum_of_squares(n, m)` that calculates the sum of squares of integers from `n` to `m` using the formula for the sum of squares of integers from 1 to `m` and from 1 to `n-1`. The function should return the result of the subtraction of the sum of squares from 1 to `n-1` from the sum of squares from 1 to `m`. Assume `n` and `m` are positive integers and `n` is less than or equal to `m`.
"""

def sum_of_squares(n, m):
    def sum_squares_to_k(k):
        return k * (k + 1) * (2 * k + 1) // 6

    return sum_squares_to_k(m) - sum_squares_to_k(n - 1)