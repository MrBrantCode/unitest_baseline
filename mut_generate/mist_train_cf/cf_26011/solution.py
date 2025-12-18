"""
QUESTION:
Write a function called `find_median` that takes a list of numbers as input and returns the median. The list of numbers can contain an odd or even number of elements, and the median should be calculated accordingly. The input list is not guaranteed to be sorted.
"""

def find_median(nums):
    """
    Calculate the median of a list of numbers.

    Args:
    nums (list): A list of numbers.

    Returns:
    float: The median of the input list.
    """
    nums = sorted(nums)
    n = len(nums)

    if n % 2 == 0:
        median = (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        median = nums[n//2]

    return median