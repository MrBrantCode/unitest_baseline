"""
QUESTION:
Write a function `maxRainwater(elevation)` that takes an array of non-negative integers representing elevations of structures, and returns the maximum volume of rainwater that can be captured between two structures. The input array `elevation` has a length `n` between 2 and 10^5, and each integer in the array is between 0 and 10^4.
"""

def maxRainwater(elevation):
    left = 0
    right = len(elevation) - 1
    max_left = max_right = max_water = 0
    
    while left < right:
        if elevation[left] < elevation[right]:
            if elevation[left] > max_left:
                max_left = elevation[left]
            else:
                max_water += max_left - elevation[left]
            left += 1
        else:
            if elevation[right] > max_right:
                max_right = elevation[right]
            else:
                max_water += max_right - elevation[right]
            right -= 1

    return max_water