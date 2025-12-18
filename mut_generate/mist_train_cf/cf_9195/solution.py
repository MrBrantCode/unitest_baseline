"""
QUESTION:
Given an array of integers, write a function `max_product_of_three` that returns the maximum product of three integers in the array. The array is guaranteed to contain at least three integers.
"""

def max_product_of_three(nums):
    nums.sort()  # sort the array in ascending order
    n = len(nums)
    return nums[n-1] * nums[n-2] * nums[n-3]  # return the product of last three integers