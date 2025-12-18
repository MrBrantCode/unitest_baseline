"""
QUESTION:
Write a function `length_of_LIS(nums)` that takes an array of integers `nums` as input and returns the length of the longest increasing subsequence within the array. The function should have a time complexity of O(n^2) or better, where n is the length of the input array.
"""

def length_of_LIS(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)