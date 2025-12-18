"""
QUESTION:
Write a function `cumulative_sum` that takes a list of numerical strings as input, transforms them into whole numbers, reverses their order, excludes the two smallest values, and returns the cumulative sum of the remaining numbers. The function should assume the list contains at least three elements.
"""

def cumulative_sum(lst):
    """
    This function transforms a list of numerical strings into whole numbers, 
    reverses their order, excludes the two smallest values, and returns 
    the cumulative sum of the remaining numbers.

    Parameters:
    lst (list): A list of numerical strings.

    Returns:
    int: The cumulative sum of the remaining numbers.
    """
    return sum(sorted(map(int, lst), reverse=True)[:-2])