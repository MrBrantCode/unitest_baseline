"""
QUESTION:
Write a function `max_product_pair(nums)` that takes an array of integers `nums` and returns a pair of integers from the array with the maximum product. The function should handle cases where the array contains two large negative numbers.
"""

def max_product_pair(nums):
    nums.sort()
    min_product = nums[0] * nums[1]
    max_product = nums[-1] * nums[-2]
    
    if min_product > max_product:
        return [nums[0], nums[1]]
    else:
        return [nums[-1], nums[-2]]