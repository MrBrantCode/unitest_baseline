"""
QUESTION:
Write a function `constrainedSubsetSum(nums, k, m)` that takes an integer array `nums`, two integers `k` and `m`, and returns the maximum sum of a non-empty subsequence from the array such that for every pair of consecutive integers in the subsequence, `j - i <= k` holds true and the sum of the subsequence does not surpass `m`. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the size of the input array. The input constraints are `1 <= k <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`, and `-10^4 <= m <= 10^4`.
"""

import heapq
def constrainedSubsetSum(nums, k, m):
    n = len(nums)
    dp, queue = [0]*n, []
    dp[0] = nums[0]
    heapq.heappush(queue, [-dp[0], 0])
    for i in range(1, n):
        while queue and queue[0][1] < i-k: heapq.heappop(queue)
        dp[i] = nums[i]
        if queue: dp[i] = max(dp[i], nums[i] - queue[0][0])
        if dp[i] > m: return m
        if dp[i] > 0: heapq.heappush(queue, [-dp[i], i])
    return max(dp)