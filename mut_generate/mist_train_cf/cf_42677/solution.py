"""
QUESTION:
Implement the function `longest_increasing_subsequence(nums)` which takes a list of integers `nums` as input and returns the longest increasing subsequence. The input list has a length between 0 and 1000, and each element is within the range [-10^9, 10^9]. If there are multiple longest increasing subsequences, any one can be returned.
"""

from typing import List

def longest_increasing_subsequence(nums: List[int]) -> List[int]:
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_len = 1
    end_index = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
                if dp[i] > max_len:
                    max_len = dp[i]
                    end_index = i

    result = []
    while end_index != -1:
        result.append(nums[end_index])
        end_index = prev[end_index]

    return result[::-1]