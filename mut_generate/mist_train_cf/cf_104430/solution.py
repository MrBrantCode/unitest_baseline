"""
QUESTION:
Calculate the median of a list of integers, considering that the list may contain duplicates. The median should be the middle element if the list length is odd, and the average of the two middle elements if the list length is even. Implement a function `calculate_median` that takes a list of integers as input and returns the calculated median.
"""

def calculate_median(numbers):
    """
    Calculate the median of a list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The median of the list of integers.
    """
    # Sort the list of integers in ascending order
    numbers.sort()

    # Get the length of the list
    n = len(numbers)

    # If the length of the list is odd, the median is the middle element
    if n % 2 != 0:
        # The index of the middle element is (n - 1) / 2
        median = numbers[n // 2]
    # If the length of the list is even, the median is the average of the two middle elements
    else:
        # The indices of the two middle elements are n / 2 - 1 and n / 2
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    return median