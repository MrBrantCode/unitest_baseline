"""
QUESTION:
Write a function called `remove_first_even` that takes a list of integers as input. The list must contain at least 5 elements. If the first element is even, the function should return a new list that contains all elements from the input list except the first one. If the first element is odd, the function should return the original list unchanged.
"""

def remove_first_even(nums):
    """
    This function takes a list of integers as input and returns a new list.
    If the first element is even, it returns a new list with all elements except the first one.
    If the first element is odd, it returns the original list unchanged.

    Args:
        nums (list): A list of integers with at least 5 elements.

    Returns:
        list: A new list based on the parity of the first element in the input list.
    """
    if nums[0] % 2 == 0:
        return nums[1:]
    else:
        return nums