"""
QUESTION:
Write a function `sum_pow3(n)` that takes an integer `n` and returns the sum of all powers of 3 that are less than or equal to `n`, modulo 987654321. The function should use a loop to calculate the sum. The result should be the value of `T(n)` in the given problem.
"""

def sum_pow3(n):
    p, sum, mod = 1, 0, 987654321
    while p <= n:
        sum = (sum + p) % mod
        p *= 3
    return sum