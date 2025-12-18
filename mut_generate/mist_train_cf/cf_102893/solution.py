"""
QUESTION:
Compute the mean of a given set of numbers. The function should be named `compute_mean`. It should take a list of numbers as input and return the mean of the numbers. The mean is calculated by summing up all the numbers and then dividing the sum by the total number of numbers.
"""

def compute_mean(numbers):
    """
    This function calculates the mean of a given set of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    return sum(numbers) / len(numbers)