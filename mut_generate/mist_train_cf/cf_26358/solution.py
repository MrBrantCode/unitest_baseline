"""
QUESTION:
Write a function named `sort_ascending` that takes a list of integers as input and returns the sorted list in ascending order without using any built-in sorting functions. The input list will contain at least two elements, and the function should modify the original list.
"""

def sort_ascending(nums):
    """
    Sorts a list of integers in ascending order without using built-in sorting functions.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: The sorted list in ascending order.
    """
    # Iterate through the list
    for i in range(len(nums)):
        # Last i elements are already in place
        for j in range(len(nums) - i - 1):
            # Traverse the list from 0 to len(nums)-i-1
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j + 1]:
                # Swap the elements
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums