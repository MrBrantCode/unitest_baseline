"""
QUESTION:
Given an integer array `nums` and two integers `k` and `m`, write a function `checkSubarraySum` that returns `true` if `nums` has a continuous subarray of size at least `m` whose elements sum up to a multiple of `k`, or `false` otherwise. The function should have a time complexity of O(n), where n is the length of the given array.

Restrictions: `1 <= len(nums) <= 10^5`, `0 <= nums[i] <= 10^9`, `0 <= sum(nums[i]) <= 2^31 - 1`, `1 <= k, m <= 2^31 - 1`.
"""

def checkSubarraySum(nums, k, m):
    if len(nums) < m: 
        return False 

    # dictionary to store the remainder when current sum is divided by k and its corresponding index
    mod_dict = {0: -1} # Initialize with zero sum at the index of -1

    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        remainder = curr_sum % k 

        # if remainder has been seen before check if the difference between current index and last index is greater than or equal to m
        if remainder in mod_dict and i - mod_dict[remainder] >= m:
            return True 
        elif remainder not in mod_dict: 
            # only update the first seen index of this remainder
            mod_dict[remainder] = i  

    return False