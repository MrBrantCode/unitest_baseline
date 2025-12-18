"""
QUESTION:
Write a function `find_median` that calculates the median of a given list of numbers. The list may contain any number of integers, and the function should return the median value. If the list has an odd number of values, the median is the middle value. If the list has an even number of values, the median is the average of the two middle values.
"""

def find_median(nums):
    """
    This function calculates the median of a given list of numbers.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    float: The median value of the input list.
    """
    nums.sort()
    length = len(nums)
    
    # If the list has an odd number of values, the median is the middle value
    if length % 2 != 0:
        return nums[length // 2]
    # If the list has an even number of values, the median is the average of the two middle values
    else:
        mid1 = nums[length // 2 - 1]
        mid2 = nums[length // 2]
        return (mid1 + mid2) / 2