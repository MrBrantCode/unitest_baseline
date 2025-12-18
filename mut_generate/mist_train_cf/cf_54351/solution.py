"""
QUESTION:
Write a function `checkSubarraySum` that takes an integer array `nums` and an integer `k` as input, and returns `True` if `nums` has a continuous subarray of size at least two whose elements sum up to a multiple of `k` with no duplicate elements, and `False` otherwise. The constraints are `1 <= len(nums) <= 10^5`, `0 <= nums[i] <= 10^9`, `0 <= sum(nums) <= 2^31 - 1`, and `1 <= k <= 2^31 - 1`.
"""

def checkSubarraySum(nums, k):
    hashmap = {0: -1}
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        prefix_sum %= k
        if prefix_sum in hashmap and i - hashmap[prefix_sum] > 1:
            return True
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i
    return False