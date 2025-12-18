"""
QUESTION:
Given a sorted list of integers, implement the function `removeDuplicates` that removes duplicates in-place such that each element appears only once and returns the new length of the list. The function should not allocate extra space for another list and must modify the input list in-place with O(1) extra memory.
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    # Initialize the pointer for the new length
    new_length = 1
    
    # Iterate through the array
    for i in range(1, len(nums)):
        # If the current element is different from the previous one
        if nums[i] != nums[i-1]:
            # Update the array in-place
            nums[new_length] = nums[i]
            # Increment the new length pointer
            new_length += 1
    
    return new_length