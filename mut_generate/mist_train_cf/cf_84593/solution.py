"""
QUESTION:
Write a function `maxProduct(nums)` that takes a list of integers as input and returns the maximum product of a contiguous subarray within the given array. The function should handle cases where the input array is empty, and should return 0 in such cases.
"""

def maxProduct(nums):
    if not nums:
        return 0

    max_so_far = min_so_far = result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        max_so_far = max(nums[i], max_so_far * nums[i])
        min_so_far = min(nums[i], min_so_far * nums[i])

        result = max(result, max_so_far)

    return result