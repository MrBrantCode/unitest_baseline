"""
QUESTION:
Write a function `find_largest_number` that takes a list as input and returns the largest integer in the list, ignoring non-integer elements. The function should handle negative numbers and duplicates, and it should have a time complexity of O(n). Do not use any built-in sorting or max functions.
"""

def find_largest_number(lst):
    """
    Returns the largest integer in the list, ignoring non-integer elements.

    Args:
        lst (list): The input list containing integers and possibly non-integer elements.

    Returns:
        int: The largest integer in the list. If the list is empty or contains no integers, returns negative infinity.
    """
    largest_number = float('-inf')
    for num in lst:
        if isinstance(num, int):
            if largest_number == float('-inf'):
                largest_number = num
            else:
                largest_number = largest_number if largest_number > num else num
    return largest_number