"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input, removes duplicates, sorts the list in ascending order, and returns the count of unique numbers. The function should be able to handle negative integers and zero.
"""

def remove_duplicates(numbers):
    """
    Removes duplicates from a list of integers, sorts the list in ascending order, and returns the count of unique numbers.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The count of unique numbers in the list.
    """
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return len(unique_numbers)