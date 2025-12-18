"""
QUESTION:
Write a function `third_smallest` that takes a list of numbers `nums` and a range `range_nums` as input. The function should return the third smallest number in `nums` that falls within the range (exclusive) defined by `range_nums`. If there are less than three numbers in the given range, the function should return an error message.
"""

def third_smallest(nums, range_nums):
    """
    Returns the third smallest number in `nums` that falls within the range (exclusive) defined by `range_nums`.
    
    Args:
    nums (list): A list of numbers.
    range_nums (list): A list containing the start and end of the range (exclusive).
    
    Returns:
    The third smallest number in the given range, or an error message if there are less than three numbers in the range.
    """
    new_list = [i for i in nums if i > range_nums[0] and i < range_nums[1]]
    new_list.sort()
    if len(new_list) >= 3:
        return new_list[2]
    else:
        return "There are less than 3 numbers in the given range."