"""
QUESTION:
Write a function `trapped_rainwater(rains)` that calculates the total amount of trapped rainwater given a list of integers representing daily rainfall amounts. The function should take in the list of rainfall amounts and return the total trapped rainwater. The input list represents the height of each bar in a histogram, where the width of each bar is 1 unit. The function should calculate the total area of water that can be trapped between the bars. The input list will contain at least one element, and all elements will be non-negative integers.
"""

from typing import List

def trappedRainWater(rains: List[int]) -> int:
    n = len(rains)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    # Calculate the maximum height to the left of each element
    left_max[0] = rains[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], rains[i])

    # Calculate the maximum height to the right of each element
    right_max[n-1] = rains[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], rains[i])

    # Calculate the trapped rainwater for each element
    for i in range(n):
        water_trapped += max(0, min(left_max[i], right_max[i]) - rains[i])

    return water_trapped