"""
QUESTION:
Write a function `find_median` that calculates and returns the median of a given list of numbers. The list is already sorted in ascending order. If the list length is odd, return the middle number. If the list length is even, return the average of the two middle numbers.
"""

def find_median(nums):
    """
    Calculate and return the median of a given list of numbers.
    
    The list is already sorted in ascending order. If the list length is odd, 
    return the middle number. If the list length is even, return the average 
    of the two middle numbers.

    Args:
        nums (list): A sorted list of numbers.

    Returns:
        float: The median of the given list of numbers.
    """
    middle_index = len(nums) // 2
    if len(nums) % 2:  
        return nums[middle_index]
    else:  
        return (nums[middle_index - 1] + nums[middle_index]) / 2.0