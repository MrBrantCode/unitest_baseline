"""
QUESTION:
Design a function `remove_duplicates(nums)` that removes all duplicates from an unsorted array of integers in-place. The function should have a time complexity of O(n), where n is the number of elements in the array, and return the updated length of the array after removing duplicates.
"""

def entance(nums):
    unique_nums = set()
    last_non_duplicate = 0
    
    for i in range(len(nums)):
        if nums[i] not in unique_nums:
            unique_nums.add(nums[i])
            nums[last_non_duplicate] = nums[i]
            last_non_duplicate += 1
    
    del nums[last_non_duplicate:]
    
    return last_non_duplicate