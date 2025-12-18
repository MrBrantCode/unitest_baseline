"""
QUESTION:
Design a function `longest_increasing_subsequence` that takes a list of integers as input and returns the longest increasing subsequence. The function should return one of the longest increasing subsequences if there are multiple. The time complexity should be O(n^2), where n is the length of the input list.
"""

def longest_increasing_subsequence(nums):
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n 

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    result = []
    for i in reversed(range(n)):
        if dp[i] == max_length:
            result.append(nums[i])
            max_length -= 1
    return result[::-1]