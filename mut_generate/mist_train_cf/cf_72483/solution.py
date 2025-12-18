"""
QUESTION:
Write a function named `harmonic_sum(n)` that calculates the harmonic sum of `n-1` using recursion. The harmonic sum is the sum of the reciprocals of the first `n-1` positive integers. For example, `harmonic_sum(4)` should return `1 + 1/2 + 1/3 + 1/4`. The function should work for `n >= 1` and use recursion to calculate the sum.
"""

def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)