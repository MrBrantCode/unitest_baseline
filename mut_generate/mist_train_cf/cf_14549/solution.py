"""
QUESTION:
Write a function called `search_integer` to find the index of the first occurrence of a target integer in a given list of integers. The list may contain duplicate values. If the target integer exists, return its index; otherwise, return -1.
"""

def search_integer(nums, target):
    """
    Find the index of the first occurrence of a target integer in a given list of integers.
    
    Args:
        nums (list): A list of integers.
        target (int): The target integer to be searched.
    
    Returns:
        int: The index of the first occurrence of the target integer if found; otherwise, -1.
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1