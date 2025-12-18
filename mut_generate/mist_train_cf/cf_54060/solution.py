"""
QUESTION:
Given an integer array `nums` and two integers `k` and `m`, write a function `constrainedSubsetSum(nums, k, m)` that returns the maximum sum of a non-empty subsequence of `nums` such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied, and the sum of the subsequence does not exceed `m`.

Constraints: `1 <= k <= nums.length <= 10^5` and `-10^4 <= nums[i], m <= 10^4`.
"""

import heapq

def constrainedSubsetSum(nums, k, m):
    n = len(nums)
    dp = [0] * n
    heap = []
    res = float('-inf')
    for i in range(n):
        while heap and i - heap[0][1] > k:
            heapq.heappop(heap)
                
        cur_max = nums[i] + (heap[0][0] if heap else 0)
        dp[i] = cur_max
        res = max(res, cur_max)
        if cur_max > m:
            break

        if cur_max > 0:
            heapq.heappush(heap, (-cur_max, i))
            
    return min(res, m)