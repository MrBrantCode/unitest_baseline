"""
QUESTION:
Write a function named `second_smallest` that takes a list of integers as input, removes duplicates, and returns the second smallest unique number. If the list contains less than 2 unique numbers, return a message indicating this. The function should be able to handle both positive and negative integers.
"""

def second_smallest(nums):
    """
    This function takes a list of integers, removes duplicates, 
    and returns the second smallest unique number.

    Args:
        nums (list): A list of integers.

    Returns:
        int or str: The second smallest unique number, or a message if the list contains less than 2 unique numbers.
    """
    unique_nums = list(set(nums))  # remove duplicates
    unique_nums.sort()  # sort the list
    if len(unique_nums) >= 2:
        return unique_nums[1]  # return the second number
    else:
        return 'Array has less than 2 unique numbers!'