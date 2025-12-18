"""
QUESTION:
Given an array of integers representing building heights, write a function `max_area(height)` that calculates the maximum amount of rainwater that can be trapped between the buildings. The function should take the array `height` as input and return the maximum amount of water that can be trapped. The length of the array `n` is in the range 2 to 10^5, and each building height is in the range 0 to 10^4.
"""

def max_area(height):
    
    maxWater = 0
    left = 0
    right = len(height) - 1

    while (left < right):
        
        maxWater = max(maxWater, min(height[left], height[right]) * (right - left))
 
        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1

    return maxWater