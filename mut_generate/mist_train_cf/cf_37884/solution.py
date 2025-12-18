"""
QUESTION:
Given a list of non-negative integers representing building heights, where the width of each building is 1 unit, write a function `trapped_rainwater` that calculates the total amount of rainwater that can be trapped between the buildings. The function should return the total trapped rainwater. 

Function signature: `def trapped_rainwater(heights: List[int]) -> int`
"""

from typing import List

def trapped_rainwater(heights: List[int]) -> int:
    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])

    right_max[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - heights[i]

    return water_trapped