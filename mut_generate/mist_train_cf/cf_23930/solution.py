"""
QUESTION:
Design a function named `find_maximum` that takes a list of integers as input and returns the maximum number in the list. The function should iterate through each number in the list and keep track of the maximum value found so far.
"""

def find_maximum(numbers):
    """
    This function finds the maximum number in a given list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The maximum number in the list.
    """
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum