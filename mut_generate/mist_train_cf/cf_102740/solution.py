"""
QUESTION:
Implement a function `group_numbers` that takes a list of integers as input and returns a list of lists, where each sublist contains three consecutive elements from the input list, starting from the second element. If the input list has a length that is not a multiple of 3, the remaining elements should be included in the last sublist.
"""

def group_numbers(nums):
    """
    This function takes a list of integers as input and returns a list of lists.
    Each sublist contains three consecutive elements from the input list, 
    starting from the second element. If the input list has a length that is 
    not a multiple of 3, the remaining elements should be included in the last sublist.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of lists, where each sublist contains three consecutive elements.
    """
    return [nums[i:i+3] for i in range(1, len(nums), 3)]