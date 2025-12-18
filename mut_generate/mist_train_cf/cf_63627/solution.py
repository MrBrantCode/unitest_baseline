"""
QUESTION:
Write a function `find_max_sum` that takes an array of integers `nums` as input and returns the maximum sum of a subarray with no two elements being adjacent. The function should run in linear time complexity and use linear extra space. If the input array is empty, return 0.
"""

def find_max_sum(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]