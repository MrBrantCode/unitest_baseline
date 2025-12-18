"""
QUESTION:
Given a function `containsNearbyDuplicate(nums, k)`, determine if there are two distinct indices i and j in the array `nums` such that `nums[i] = nums[j]` and the absolute difference between i and j is at most k. The input array `nums` contains at most 10^6 elements, all elements are between -10^6 and 10^6, and the function should run in linear time complexity O(n), where n is the number of elements in the array.
"""

def containsNearbyDuplicate(nums, k):
    num_indices = {}  # hash table to store indices of elements

    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i

    return False