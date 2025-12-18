"""
QUESTION:
Write a function `remove_element` that removes all occurrences of a given element from a list in-place while maintaining the original order of the remaining elements. The function should have a time complexity of O(n) and should not create a new list or use additional data structures.
"""

def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return nums