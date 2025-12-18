"""
QUESTION:
Given an integer array `nums` and an integer `k`, return the maximum length of a subarray that sums to `k`. If there isn't one, return `0` instead. Additionally, return the starting and ending indices of the longest subarray. If there are multiple subarrays with the same maximum length, return the indices of the first one you find.

The function `maxSubArrayLen(nums, k)` should take an integer array `nums` and an integer `k` as inputs and return a tuple where the first element is the length of the longest subarray sum as `k` and the second element is a list containing the starting and ending indices.

Constraints: `1 <= nums.length <= 104`, `-104 <= nums[i] <= 104`, `-105 <= k <= 105`. The function should run in `O(n)` time and `O(n)` space.
"""

def maxSubArrayLen(nums, k):
    sum_map = {0: -1}
    sum = 0
    max_len = 0
    indices = [0, 0]
    for i in range(len(nums)):
        sum += nums[i]
        if sum not in sum_map:
            sum_map[sum] = i
        if sum - k in sum_map:
            if max_len < i - sum_map[sum - k]:
                max_len = i - sum_map[sum - k]
                indices = [sum_map[sum - k] + 1, i]

    if max_len == 0:
        return 0, []
    else:
        return max_len, indices