"""
QUESTION:
Write a Python function `max_min_subarray_product(nums)` that takes a list of integers `nums` as input and returns a tuple containing the maximum and minimum product of a subarray in the input list. The function should handle negative numbers and zeroes efficiently.
"""

def max_min_subarray_product(nums):
    # Initialize the maximum and minimum product up to the current position
    max_dp = [0] * len(nums)
    min_dp = [0] * len(nums)

    # The maximum and minimum product for the first number is the number itself
    max_dp[0] = min_dp[0] = nums[0]

    for i in range(1, len(nums)):
        # When num[i] is positive, the maximum product can be get by multiplying the previous maximum product
        # When num[i] is negative, the maximum product can be get by multiplying the previous minimum product
        max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])
        # Similarly for min_dp
        min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])

    # Return the maximum product and minimum product
    return (max(max_dp), min(min_dp))