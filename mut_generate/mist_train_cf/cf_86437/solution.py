"""
QUESTION:
Write a function called `find_max_indices` that takes an array of positive integers as input and returns the indices of all occurrences of the maximum number in ascending order. The function should handle arrays of any size with a time complexity of O(n) and return an empty list if the input array is empty.
"""

def find_max_indices(nums):
    if not nums:
        return []
    
    max_num = max(nums)
    indices = [i for i, num in enumerate(nums) if num == max_num]
    return indices