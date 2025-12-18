"""
QUESTION:
Given an integer array `nums` and three integers `k`, `t`, and `p`, write a function `containsNearbyAlmostDuplicate` that returns `true` if there are two distinct indices `i` and `j` in the array such that `abs(nums[i] - nums[j]) <= t` and `abs(i - j) <= k` and `abs(nums[i] - p) <= t`, and `false` otherwise. The function should handle the constraints: `0 <= nums.length <= 2 * 10^4`, `-2^31 <= nums[i] <= 2^31 - 1`, `0 <= k <= 10^4`, `0 <= t <= 2^31 - 1`, and `-2^31 <= p <= 2^31 - 1`.
"""

def containsNearbyAlmostDuplicate(nums, k, t, p):
    if t < 0: 
        return False
    num_dict = {}
    w = t + 1
    for i in range(len(nums)):
        m = nums[i] // w
        if m in num_dict:
            return True
        if m - 1 in num_dict and abs(nums[i] - num_dict[m - 1]) < w:
            return True
        if m + 1 in num_dict and abs(nums[i] - num_dict[m + 1]) < w:
            return True
        if abs(nums[i] - p) > t:
            return False
        num_dict[m] = nums[i]
        if i >= k: 
            del num_dict[nums[i - k] // w]
    return False