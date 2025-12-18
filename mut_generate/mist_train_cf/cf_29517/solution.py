"""
QUESTION:
Write a function `trapped_water` that takes a list of integers representing building heights, where each building's width is 1 unit, and returns the total amount of water that can be trapped between the buildings. The function should consider that water is trapped if there are higher buildings on both sides of a building. The input list will contain at least one element.
"""

from typing import List

def trapped_water(height: List[int]) -> int:
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    # Calculate the maximum height to the left of each building
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    # Calculate the maximum height to the right of each building
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    # Calculate the trapped water for each building
    for i in range(n):
        water_trapped += max(0, min(left_max[i], right_max[i]) - height[i])

    return water_trapped