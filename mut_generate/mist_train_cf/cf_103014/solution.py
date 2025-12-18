"""
QUESTION:
Write a function `containsNearbyDuplicate` that takes an array of integers `nums` and an integer `k` as input, and returns `True` if there exist two distinct indices `i` and `j` in the array such that `nums[i] = nums[j]` and the absolute difference between `i` and `j` is at most `k`. The function should have a time complexity of O(n), where n is the number of elements in the array. The array will have at most 10^5 elements and all elements will be between -10^5 and 10^5.
"""

def containsNearbyDuplicate(nums, k):
    """
    Checks if there exist two distinct indices i and j in the array such that nums[i] = nums[j] 
    and the absolute difference between i and j is at most k.

    Args:
    nums (list): An array of integers.
    k (int): The maximum absolute difference between the indices.

    Returns:
    bool: True if a pair of indices that satisfy the condition exist, False otherwise.
    """
    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap and i - hashmap[num] <= k:
            return True
        hashmap[num] = i
    return False