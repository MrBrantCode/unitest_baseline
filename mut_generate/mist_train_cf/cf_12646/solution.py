"""
QUESTION:
Write a function `find_largest_even` that takes a list of integers as input and returns the largest even number in the list. If the list contains no even numbers, the function should return a message indicating that.
"""

def find_largest_even(lst):
    """
    This function takes a list of integers as input and returns the largest even number in the list.
    If the list contains no even numbers, the function returns a message indicating that.

    Args:
        lst (list): A list of integers.

    Returns:
        int or str: The largest even number in the list, or a message if no even numbers are found.
    """
    even_nums = [num for num in lst if num % 2 == 0]
    if even_nums:
        return max(even_nums)
    else:
        return "No even numbers found in the list."