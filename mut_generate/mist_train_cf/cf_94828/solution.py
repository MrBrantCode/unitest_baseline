"""
QUESTION:
Write a function `containsNearbyDuplicate(nums, k)` that determines if there are two distinct indices i and j in the array `nums` such that `nums[i] = nums[j]` and the absolute difference between i and j is at most `k`. The input array will have at most 10^6 elements, with values between -10^6 and 10^6. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def containsNearbyDuplicate(nums, k):
    num_indices = {}  

    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i

    return False