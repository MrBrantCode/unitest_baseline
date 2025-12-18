"""
QUESTION:
Write a function `move_zeros(nums)` that takes an array of integers as input and returns the array with all zeros moved to the end, while maintaining the original order of non-zero numbers. The input array is not empty and contains only integers.
"""

def move_zeros(nums):
    # List comprehesion - It will first put all non-zero numbers, then append zeros to the end
    return [num for num in nums if num != 0] + [0] * nums.count(0)