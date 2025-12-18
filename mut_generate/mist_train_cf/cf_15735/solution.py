"""
QUESTION:
Write a function named `remove_element` that takes two parameters: a list `nums` and a value `val`. The function should remove all occurrences of `val` from `nums` and return the modified list. The function should have a time complexity of O(n), where n is the length of the list, and a space complexity of O(1). Do not use any built-in Python functions or methods for removing elements from a list.
"""

def remove_element(nums, val):
    i, j = 0, 0
    n = len(nums)
    
    while j < n:
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        j += 1
    
    nums = nums[:i]
    
    return nums