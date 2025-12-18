"""
QUESTION:
Create a function `filter_and_sort_list` that takes a list of integers as input, removes elements that are either not even or greater than 5, and returns the modified list in descending order. The input list should not be modified in-place.
"""

def filter_and_sort_list(nums):
    """
    This function filters a list of integers to include only even numbers less than or equal to 5,
    and returns the modified list in descending order.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The modified list of integers.
    """
    # Create a new list to avoid modifying the input list in-place
    filtered_list = [num for num in nums if num % 2 == 0 and num <= 5]
    
    # Sort the filtered list in descending order
    filtered_list.sort(reverse=True)
    
    return filtered_list