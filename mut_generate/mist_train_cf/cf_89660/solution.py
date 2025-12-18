"""
QUESTION:
Implement a function `complement` that returns the complement of a given list `nums` without using any built-in functions or methods. The complement of a binary list is a list where each 0 is replaced with a 1 and each 1 is replaced with a 0. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list, and should be implemented using a recursive approach.
"""

def complement(nums):
    if not nums:
        return []

    rest = complement(nums[1:])
    rest.insert(0, 1 - nums[0])
    
    return rest