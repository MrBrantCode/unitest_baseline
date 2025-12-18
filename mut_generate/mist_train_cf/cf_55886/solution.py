"""
QUESTION:
Implement a function named `compute_aggregate(m, n)` that calculates the sum of all integers from `m` to `n` (inclusive), where `m` and `n` are the input parameters. The function should return the aggregate sum.
"""

def compute_aggregate(m, n):
    return sum(range(m, n+1))