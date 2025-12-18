"""
QUESTION:
Write a function `find_max_indices` that takes an array of positive integers as input and returns the indices of all occurrences of the maximum number in ascending order. If the input array is empty, return an empty list. The function should have a time complexity of O(n), where n is the size of the input array.
"""

def find_max_indices(nums):
    if not nums:
        return []
    
    max_num = max(nums)
    indices = [i for i, num in enumerate(nums) if num == max_num]
    return indices