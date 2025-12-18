"""
QUESTION:
Write a function `containsNearbyAlmostDuplicate(nums, k, m)` that determines if there exist two unique indices `i` and `j` within the array `nums` such that `nums[i] equals nums[j]`, the absolute difference between `i` and `j` is less than or equal to `k`, and the sum of `nums[i]` and `nums[j]` is divisible by `m`.

Constraints:
- The length of `nums` is between 1 and 10^5 inclusive.
- The elements of `nums`, `nums[i]`, are between -10^9 and 10^9 inclusive.
- `k` and `m` are non-negative integers and can go up to 10^5.
"""

from collections import OrderedDict

def containsNearbyAlmostDuplicate(nums, k, m):
    if m == 0:
        return False
    dict_nums = OrderedDict()
    for i in range(len(nums)):
        mod_nums = nums[i] % m
        if mod_nums in dict_nums:
            if i - dict_nums[mod_nums][1] <= k and (nums[i] + dict_nums[mod_nums][0]) % m == 0:
                return True
            dict_nums.popitem(last=False)
        dict_nums[mod_nums] = (nums[i], i)
    return False