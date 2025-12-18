"""
QUESTION:
Write a function `max_product_subarray(nums)` that takes a list of integers `nums` as input and returns the maximum product of all possible subarrays within `nums`. A subarray is a contiguous segment of elements in the original array. The function should handle cases where the input array is empty and return 0 in such cases.
"""

def max_product_subarray(nums):
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])

        result = max(result, max_prod)

    return result