"""
QUESTION:
Write a function `trapped_rainwater` that calculates the total amount of rainwater that can be trapped between a series of buildings, given a list of integers representing the heights of the buildings, where the width of each building is 1 unit. The function should return the total trapped rainwater. The input list contains non-negative integers and has at least 3 elements.
"""

from typing import List

def trapped_rainwater(heights: List[int]) -> int:
    n = len(heights)
    if n < 3:
        return 0

    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = heights[0]
    right_max[n - 1] = heights[n - 1]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    total_rainwater = 0
    for i in range(n):
        total_rainwater += max(0, min(left_max[i], right_max[i]) - heights[i])

    return total_rainwater