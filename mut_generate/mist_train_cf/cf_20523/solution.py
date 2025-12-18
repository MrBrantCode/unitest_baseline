"""
QUESTION:
Write a function, `get_unique_odd_numbers`, that takes a list of integers as input and returns a new list containing the unique odd numbers from the original list, without using any built-in functions or libraries to remove duplicates. The function should have a time complexity of O(n^2) or less.
"""

def get_unique_odd_numbers(lst):
    """
    Returns a new list containing the unique odd numbers from the original list.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A list of unique odd numbers.
    """
    unique_odd_numbers = []
    for num in lst:
        if num % 2 != 0:
            if num not in unique_odd_numbers:
                unique_odd_numbers.append(num)
    return unique_odd_numbers