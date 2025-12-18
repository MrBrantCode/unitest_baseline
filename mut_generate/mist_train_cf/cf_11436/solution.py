"""
QUESTION:
Create a function called `calculate_median` that takes a list of integers as input and returns the median of the list. The function should arrange the list in ascending order and determine the middle number(s) to calculate the median. If the list has an odd number of integers, the median is the middle number. If the list has an even number of integers, the median is the average of the two middle numbers.
"""

def calculate_median(numbers):
    """
    Calculate the median of a list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    float: The median of the list of integers.
    """
    # Arrange the list in ascending order
    numbers.sort()

    # Get the length of the list
    n = len(numbers)

    # If the list has an odd number of integers, the median is the middle number
    if n % 2 != 0:
        # The median is the middle number
        median = numbers[n // 2]
    else:
        # If the list has an even number of integers, the median is the average of the two middle numbers
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        # Calculate the average
        median = (mid1 + mid2) / 2

    return median