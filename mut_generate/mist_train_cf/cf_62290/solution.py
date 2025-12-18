"""
QUESTION:
Write a function `smallest_subset(matrix, target)` that takes a 2D list `matrix` and an integer `target` as input. The function should return the smallest number of elements in the matrix that sum up to `target`. If no such combination exists, return -1.
"""

from itertools import chain

def smallest_subset(matrix, target):
    flat_list = list(chain.from_iterable(matrix))
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for i in range(1, target + 1):
        for num in flat_list:
            if num <= i:
                dp[i] = min(dp[i], dp[i-num] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1