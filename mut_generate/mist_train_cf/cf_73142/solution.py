"""
QUESTION:
The function `cumulative_sum(n)` should calculate the sum of `R(n^3)` for `1 ≤ n < n`. Here, `R(n)` is defined as `R(n) = R(n-1) - n` if `R(n-1) - n > 0` and `R(n-1) - n` is not already in the sequence, and `R(n) = R(n-1) + n` otherwise, with `R(0) = 0`. Calculate `cumulative_sum(10**6)`.
"""

def entrance(n):
    total = 0
    for i in range(1, n):
        total += (i**3 * (i**3 + 1)) // 2
    return total