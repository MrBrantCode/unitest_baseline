"""
QUESTION:
Write a function `removeDuplicates` that takes an array and its size as input. The function should remove all duplicates from the array in-place and return the length of the new array. The original array order should be preserved, and the function should not use any additional data structures.
"""

def removeDuplicates(nums):
    """
    Removes duplicates from a given list in-place and returns the length of the new list.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The length of the new list.
    """
    if not nums:
        return 0

    index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]
    return index + 1