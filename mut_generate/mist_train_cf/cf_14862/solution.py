"""
QUESTION:
Write a function called `reverseArray` that takes an array of numbers as input and reverses the order of its elements in-place without using any additional data structures.
"""

def reverseArray(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums