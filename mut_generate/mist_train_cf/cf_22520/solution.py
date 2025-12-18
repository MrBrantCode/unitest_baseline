"""
QUESTION:
Write a function `find_element` that takes a list of integers and a target integer as input, and returns the index of the target integer in the list. If the target integer is not found, return -1. The function should have a time complexity of O(n) and use recursion.
"""

def find_element(nums, target):
    def recursive_search(nums, target, index):
        # Base case: If the list is empty, the target is not found
        if index == len(nums):
            return -1
        
        # If the current element is the target, return its index
        if nums[index] == target:
            return index
        
        # Recursive case: Search the rest of the list
        return recursive_search(nums, target, index + 1)
    
    return recursive_search(nums, target, 0)