"""
QUESTION:
Given two lists of integers `a` and `b`, write a function `max_equal_sum_subarray` that returns the maximum value of `k` such that the sum of the first `k` elements in `a` is equal to the sum of the first `k` elements in `b`. If no such `k` exists, return 0. The lists `a` and `b` have the same length `n`.
"""

from typing import List

def max_equal_sum_subarray(a: List[int], b: List[int]) -> int:
    n = len(a)
    a_sum, b_sum = 0, 0
    max_k = 0
    prefix_sums = [[0, 0] for _ in range(n + 1)]  

    for i in range(n):
        a_sum += a[i]
        b_sum += b[i]
        prefix_sums[i + 1][0] = a_sum
        prefix_sums[i + 1][1] = b_sum

    for i in range(n):
        if prefix_sums[i + 1][0] == prefix_sums[i + 1][1]:
            max_k = max(max_k, i + 1)

    return max_k