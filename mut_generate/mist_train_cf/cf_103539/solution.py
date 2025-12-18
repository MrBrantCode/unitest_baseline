"""
QUESTION:
Write a function `removeDuplicates(nums)` that takes a list of integers `nums` as input, removes all duplicates, and returns the remaining distinct integers in a new list, sorted in non-decreasing order.
"""

def removeDuplicates(nums):
    """
    Removes duplicates from a list of integers and returns the remaining distinct integers in a new list, sorted in non-decreasing order.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A new list containing distinct integers from the input list, sorted in non-decreasing order.
    """
    distinct_nums = set(nums)
    sorted_nums = sorted(distinct_nums)
    return sorted_nums