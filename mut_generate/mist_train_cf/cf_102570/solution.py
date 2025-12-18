"""
QUESTION:
Write a function `group_by_five` that takes a list of integers as input. The input list must have a length that is a multiple of 15. The function should return a list of sublists where each sublist has a length that is a multiple of 5. The original list and the sublists should both be sorted in descending order.
"""

def group_by_five(nums):
    """
    This function takes a list of integers as input, where the length of the list must be a multiple of 15.
    It returns a list of sublists where each sublist has a length that is a multiple of 5.
    The original list and the sublists are both sorted in descending order.

    Args:
        nums (list): A list of integers with a length that is a multiple of 15.

    Returns:
        list: A list of sublists where each sublist has a length that is a multiple of 5.
    """

    # Sort the original list in descending order
    nums.sort(reverse=True)

    # Group the list elements into sublists of length that is a multiple of 5
    sublists = [nums[i:i+5] for i in range(0, len(nums), 5)]

    # Sort the sublists in descending order
    sublists.sort(reverse=True)

    return sublists