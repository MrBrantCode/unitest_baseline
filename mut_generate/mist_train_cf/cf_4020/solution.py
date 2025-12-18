"""
QUESTION:
Write a function `calculate_mean` that takes a list of numbers as input and returns the mean of the numbers without using any built-in functions or libraries for calculating the mean. The solution should have a time complexity of O(n) and handle cases where the list contains duplicate numbers.
"""

def calculate_mean(numbers):
    """
    Calculate the mean of a list of numbers without using any built-in functions or libraries for calculating the mean.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    total_sum = 0
    count = 0

    for num in numbers:
        total_sum += num
        count += 1

    mean = total_sum / count
    return mean