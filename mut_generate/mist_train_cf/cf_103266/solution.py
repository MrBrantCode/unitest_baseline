"""
QUESTION:
Write a function called `calculate_median` that takes a list of numbers as input and returns the median value. The function should be able to handle both even and odd number of elements in the list.
"""

def calculate_median(numbers):
    """
    Calculate the median value of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The median value of the input list.
    """
    n = len(numbers)
    sorted_numbers = sorted(numbers)

    if n % 2 == 0:
        median = (sorted_numbers[(n//2)-1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]

    return median