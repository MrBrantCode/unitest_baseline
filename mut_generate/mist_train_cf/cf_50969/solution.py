"""
QUESTION:
Write a function `longest_sequence(nums)` that takes a list of integers `nums` as input and returns the longest ascending subsequence that starts with the smallest integer and ends with the largest integer in the list. The subsequence must be strictly increasing.
"""

def longest_sequence(nums):
    if not nums:
        return []
    dp = [1] * len(nums)
    direction = [-1] * len(nums)
    max_length = 1
    max_index = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    direction[i] = j
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i
    sequence = []
    while max_index >= 0:
        sequence.append(nums[max_index])
        max_index = direction[max_index]
    return sequence[::-1]