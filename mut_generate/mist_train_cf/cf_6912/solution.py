"""
QUESTION:
Write a function `complement_recursive` that takes a list `nums` and an index `i` as input and returns the complement of the given list, where the complement of a binary number is calculated by flipping all bits (i.e., changing 1s to 0s and 0s to 1s). The function should use a recursive approach, have a time complexity of O(n), and a space complexity of O(1), where n is the length of the list. The function should not use any built-in functions or methods.
"""

def findComplement(nums, i):
    if i == len(nums):
        return []
    
    rest = findComplement(nums, i+1)
    rest.append(1 - nums[i])
    
    return rest