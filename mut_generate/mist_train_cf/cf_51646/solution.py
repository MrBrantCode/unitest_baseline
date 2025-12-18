"""
QUESTION:
Write a function `rotate(nums, steps)` that takes an array of integers `nums` and an integer `steps` as input. Rotate the array to the right by `steps` number of positions without using built-in rotation functions. The input array can contain negative integers and may not be sorted, and the function must handle large arrays efficiently. The function should return the rotated array without modifying the original array.
"""

def rotate(nums, steps):
    steps = steps % len(nums)
    pivot = len(nums) - steps
    return nums[pivot:] + nums[:pivot]