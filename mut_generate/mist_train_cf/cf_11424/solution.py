"""
QUESTION:
Write a function `replace_kth_smallest` that takes an integer array `nums` and an integer `K` as input, and replaces the Kth smallest number in the array with 0. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def replace_kth_smallest(nums, K):
    # Sort the array in ascending order
    nums.sort()
    
    # Replace the Kth smallest number with 0
    nums[K-1] = 0
    
    return nums