"""
QUESTION:
Write a function named `find_median` to determine the middle value of a list of decimal numbers when arranged in sequential order. The function should accept a list of decimal numbers as input and return the median value. The list will contain an odd number of elements.
"""

def find_median(numbers):
    """
    This function determines the middle value of a list of decimal numbers when arranged in sequential order.

    Args:
        numbers (list): A list of decimal numbers.

    Returns:
        float: The median value of the list.
    """
    # sort the list in ascending order
    numbers.sort()

    # compute the median
    median = numbers[len(numbers)//2]

    return median