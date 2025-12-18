"""
QUESTION:
Implement the function `reverse_list(nums)` that takes a list of integers `nums` as input, reverses the list in-place (i.e., modifies the original list), and returns the reversed list. The function must use only a single loop, not create any temporary variables or new lists, and have a time complexity of O(n), where n is the length of the list.
"""

def reverse_list(nums):
    """
    Reverses a list of integers in-place and returns the reversed list.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    list: The reversed list of integers.
    """
    # Find the length of the list
    length = len(nums)
    
    # Iterate over half of the list
    for i in range(length // 2):
        # Swap elements from the beginning and end of the list
        nums[i], nums[length - i - 1] = nums[length - i - 1], nums[i]
    
    return nums