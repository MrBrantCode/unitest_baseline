"""
QUESTION:
Write a function named `longest_increasing_subsequence` that takes a non-empty list of integers as input and returns the longest increasing subsequence and its length. The function should have a time complexity of O(n log n), where n is the length of the list, and use dynamic programming to achieve this time complexity. The subsequence does not have to be contiguous, but the numbers in the subsequence should appear in the same order as they do in the original list.
"""

def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    max_len_index = dp.index(max_len)

    subsequence = []
    index = max_len_index
    while index != -1:
        subsequence.append(nums[index])
        index = prev[index]
    
    return subsequence[::-1], max_len