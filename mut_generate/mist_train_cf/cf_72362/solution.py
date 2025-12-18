"""
QUESTION:
Write a function called `increasingSubsequence` that takes a non-decreasing array of positive integers `nums` and an integer `K` as input. The function should return `True` if it is possible to partition the array into one or more disjoint increasing subsequences, each of which has a length of at least `K`, and `False` otherwise.

The constraints are `1 <= nums.length <= 10^5`, `1 <= K <= nums.length`, and `1 <= nums[i] <= 10^5`.
"""

import heapq
def increasingSubsequence(nums, K):
    pq = []
    for num in nums:
        if pq and pq[0] < num:
            heapq.heappushpop(pq, num)
        else:
            heapq.heappush(pq, num)
    return len(pq) >= K