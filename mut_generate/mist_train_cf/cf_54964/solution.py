"""
QUESTION:
Write a function `numbers_from_k_to_n(k, n)` that takes two integer parameters, `k` and `n`, and returns a list of integers from `k` to `n` (inclusive) in ascending order, without skipping any integers.
"""

def entrance(k, n):
    return [i for i in range(k, n + 1)]