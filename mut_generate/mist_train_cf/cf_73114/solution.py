"""
QUESTION:
Write a function `length_of_LIS(nums)` that takes a list of integers `nums` as input and returns the length of the longest non-repeated increasing subsequence. The function should return 0 if the input list is empty.
"""

def length_of_LIS(nums):
    if not nums:
        return 0

    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)