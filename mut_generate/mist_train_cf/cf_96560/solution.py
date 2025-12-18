"""
QUESTION:
Implement a function `remove_duplicates(nums)` that takes a list of integers as input and returns a new list containing the unique elements from the input list, in the same order as they first appear. The function should run in O(N) time complexity and use constant space complexity. The solution should be implemented using a recursive approach and handle cases where the input list may contain duplicate elements.
"""

def remove_duplicates(nums):
    def remove_duplicates_recursive(nums, i, j):
        if i >= len(nums):
            return j
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        return remove_duplicates_recursive(nums, i + 1, j)
    
    if len(nums) == 0:
        return []
    
    last_index = remove_duplicates_recursive(nums, 1, 0)
    return nums[:last_index + 1]