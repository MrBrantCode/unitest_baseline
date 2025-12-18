"""
QUESTION:
Write a function named `cumulative_sum` that iteratively calculates the cumulative sum of all elements in a given array. The function should take an array of integers as input and return the cumulative sum. The function should not use any built-in sum functions.
"""

def cumulative_sum(lst):
    """
    Calculate the cumulative sum of all elements in a given array.

    Args:
    lst (list): A list of integers.

    Returns:
    int: The cumulative sum of all elements in the list.
    """
    cum_sum = 0
    for item in lst:
        cum_sum += item
    return cum_sum