"""
QUESTION:
Write a function `find_largest_even` that takes a list of integers as input and returns the largest even number(s) in the list. If there are no even numbers in the list, return a message indicating so. The function should not use any built-in functions or methods that directly solve the problem, such as `max()` or `sort()`, and should have the best possible time complexity. The function should not modify the original list.
"""

def find_largest_even(lst):
    """
    This function finds the largest even number in a given list of integers.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        The largest even number if found, otherwise a message indicating no even numbers were found.
    """
    largest_even = None
    for num in lst:
        if num % 2 == 0:
            if largest_even is None or num > largest_even:
                largest_even = num
    if largest_even is not None:
        return largest_even
    else:
        return "There are no even numbers in the list."