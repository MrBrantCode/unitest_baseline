"""
QUESTION:
Write a function named `find_median` that takes a list of integers as input, where the list has more than 5 elements, may contain both positive and negative integers, and may have duplicates. The function should return the median of the list, handling both odd and even length cases.
"""

def find_median(nums):
    """
    This function calculates the median of a given list of integers.

    Args:
    nums (list): A list of integers.

    Returns:
    float: The median of the list.
    """
    
    # Remove duplicates by converting the list to a set, then convert back to list
    nums = list(set(nums))
    
    # Sort the list in ascending order
    nums.sort()
    
    # Find the length of the list
    n = len(nums)
    
    # If the length of the list is odd, the median is the middle number
    if n % 2 != 0:
        return nums[n // 2]
    
    # If the length of the list is even, the median is the average of the two middle numbers
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2