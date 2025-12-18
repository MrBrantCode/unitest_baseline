"""
QUESTION:
Given an integer array `nums`, write a function `numberOfArithmeticSlices(nums)` that returns the number of arithmetic subarrays of `nums` and the longest length of the arithmetic subarray. The function should take into consideration that `1 <= nums.length <= 5000` and `-1000 <= nums[i] <= 1000`.
"""

def numberOfArithmeticSlices(nums):
    total = 0
    dp = [0] * len(nums)
    max_len = 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            dp[i] = dp[i - 1] + 1
            total += dp[i]
            max_len = max(max_len, dp[i] + 2)
    return total, max_len if max_len > 2 else 0