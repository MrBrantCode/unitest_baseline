"""
QUESTION:
Write a function named `maxSubArrayLen` that takes in an array of integers `nums` and an integer `k` as parameters. The function should return the length of the longest subarray within `nums` that sums up to `k`. If no such subarray exists, return 0. The function should operate in `O(n)` time complexity.

Restrictions: The length of `nums` is at least 1 and at most 10^4, each element in `nums` is at least -10^4 and at most 10^4, and `k` is at least -10^5 and at most 10^5.
"""

def maxSubArrayLen(nums, k):
    hashmap = {0: -1}   # base case
    sum_ = 0   # running sum
    max_len_subarray = 0   # max length of subarray

    for idx, num in enumerate(nums):
        sum_ += num
        if sum_ not in hashmap:
            hashmap[sum_] = idx
        if sum_ - k in hashmap:
            max_len_subarray = max(max_len_subarray, idx - hashmap[sum_ - k])

    return max_len_subarray