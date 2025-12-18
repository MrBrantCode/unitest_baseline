"""
QUESTION:
Given an integer array `nums` and an integer `k`, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied, and no two elements in the subsequence are equal. 

Constraints: 
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
All nums[i] are unique.
"""

import heapq

def constrainedSubsetSum(nums, k):
    dp = [0] * len(nums)
    max_sum = float('-inf')
    q = []

    for i in range(len(nums)):
        while q and i - q[0][1] > k:
            heapq.heappop(q)
        dp[i] = nums[i] + (q[0][0] if q else 0)
        while q and dp[i] > q[0][0]:
            heapq.heappop(q)
        heapq.heappush(q, (-dp[i], i))
        max_sum = max(max_sum, dp[i])

    return max_sum