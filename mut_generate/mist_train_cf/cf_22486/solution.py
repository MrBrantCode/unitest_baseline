"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of integers as input, removes duplicates from the list, and returns the updated list. The function should not use any additional data structures and should preserve the original order of the elements. The input list may contain negative integers and may have any length.
"""

def entance(nums):
    length = len(nums)
    if length <= 1:
        return nums
    
    for i in range(length - 1):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                nums.pop(j)
                length -= 1
                break  # Stop the inner loop and continue with the next element
    
    return nums