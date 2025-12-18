"""
QUESTION:
Write a function called `reverse_list` that takes a list of integers as input, reverses the list in-place, and returns the reversed list. The function should only use a single loop, must not use any temporary variables or create new lists, and should have a time complexity of O(n), where n is the length of the list.
"""

def reverse_list(nums):
    # Find the length of the list
    length = len(nums)
    
    # Iterate over half of the list
    for i in range(length // 2):
        # Swap elements from the beginning and end of the list
        nums[i], nums[length - i - 1] = nums[length - i - 1], nums[i]
    
    return nums