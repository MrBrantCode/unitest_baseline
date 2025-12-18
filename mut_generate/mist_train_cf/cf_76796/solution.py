"""
QUESTION:
Write a function named `find_median` that calculates the median of an array of floating point numbers. The array may be unsorted and can have any length. The function should return the median as a floating point number.
"""

def find_median(nums):
    """
    Calculate the median of an array of floating point numbers.

    Args:
        nums (list): A list of floating point numbers.

    Returns:
        float: The median of the input list.
    """
    nums.sort()  # sort the list in ascending order
    length = len(nums)
    
    if length % 2 == 0:  # if the list length is even
        mid1 = nums[length//2]
        mid2 = nums[length//2 - 1]
        median = (mid1 + mid2) / 2
    else:  # if the list length is odd
        median = nums[length//2]
        
    return median