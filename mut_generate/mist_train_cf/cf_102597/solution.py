"""
QUESTION:
Create a function `filter_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers from the input list. The output list should be sorted in ascending order and should not contain any duplicate elements.
"""

def filter_even_numbers(arr):
    """
    This function filters out the even numbers from the given list, removes duplicates, 
    and returns a new sorted list in ascending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A sorted list of unique even numbers.
    """
    return sorted(list(set([num for num in arr if num % 2 == 0])))