"""
QUESTION:
Write a function named `remove_element` that takes a list and an element as input, and returns a new list with all occurrences of the given element removed, including any duplicates. The function should have a time complexity of O(n) and not use any built-in list manipulation methods or additional data structures. The function should modify the original list in-place if possible.
"""

def remove_element(nums, val):
    if not nums:
        return 0
    
    write_idx = 0
    for read_idx in range(len(nums)):
        if nums[read_idx] != val:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
    
    return write_idx