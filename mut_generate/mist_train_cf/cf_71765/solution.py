"""
QUESTION:
Given an integer array `nums` and a positive integer `k`, return the most competitive subsequence of `nums` that is of size `k`. A subsequence `a` is considered more competitive than another subsequence `b` (both of the same length) if at the first position where `a` and `b` diverge, subsequence `a` has a number that is smaller than the corresponding number in `b`. 

Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^9`, and `1 <= k <= nums.length`.
"""

def mostCompetitive(nums, k):
    stack = []
    n = len(nums)
    for i in range(n):
        while stack and stack[-1] > nums[i] and len(stack) - 1 + n - i >= k:
            stack.pop()
        if len(stack) < k:
            stack.append(nums[i])
    return stack