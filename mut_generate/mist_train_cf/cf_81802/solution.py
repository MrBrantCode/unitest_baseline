"""
QUESTION:
Given an integer array `nums` and an integer `k`, determine the maximum number of operations that can be executed on the array, where an operation involves selecting two numbers from the array that add up to `k` and eliminating them from the array. The constraints are as follows: `1 <= nums.length <= 10^5` and `1 <= nums[i] <= 10^9` and `1 <= k <= 10^9`. Implement the function `maxOperations(nums, k)` to solve this problem.
"""

from collections import Counter
def entrance(nums, k):
    nums_map = Counter(nums)
    pair_count = 0
    for x in nums_map:
        if (k - x != x and nums_map[k - x] > 0) or (k - x == x and nums_map[x] > 1):
            pair_count += min(nums_map[x], nums_map[k - x])
            nums_map[k - x] -= min(nums_map[x], nums_map[k - x])
            nums_map[x] -= min(nums_map[x], nums_map[k - x])
    return pair_count // 2