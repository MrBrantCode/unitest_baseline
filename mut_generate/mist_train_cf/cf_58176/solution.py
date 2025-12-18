"""
QUESTION:
Write a function `containsNearbyDuplicate(nums, k)` that takes an integer array `nums` and an integer `k` as input, and returns `True` if there are two distinct indices `i` and `j` in the array such that `nums[i] = nums[j]` and the absolute difference of `i` and `j` is at most `k`, and `False` otherwise. The length of `nums` is between 1 and 10^5, and the range of `nums[i]` is between -10^9 and 10^9, and `k` is between 1 and 10^5.
"""

def containsNearbyDuplicate(nums, k):
    num_dict = dict()
    
    for i in range(len(nums)):
        if nums[i] in num_dict:
            if i - num_dict[nums[i]] <= k:
                return True
        num_dict[nums[i]] = i
    
    return False