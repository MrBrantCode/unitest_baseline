"""
QUESTION:
Create a function `calculate_statistics` that takes a set of integers as input and returns the number of positive numbers, the average of positive numbers, the maximum positive number, the minimum positive number, and the median of positive numbers. The set can contain up to 10^7 elements, and each element is an integer ranging from -10^9 to 10^9.
"""

import statistics

def calculate_statistics(numbers):
    """
    Calculate statistics for a set of integers.

    Args:
        numbers (set): A set of integers.

    Returns:
        tuple: A tuple containing the number of positive numbers, the average of positive numbers, 
        the maximum positive number, the minimum positive number, and the median of positive numbers.
    """
    positive_numbers = [num for num in numbers if num > 0]
    positive_count = len(positive_numbers)

    if positive_count == 0:
        return 0, 0, 0, 0, 0

    positive_sum = sum(positive_numbers)
    maximum = max(positive_numbers)
    minimum = min(positive_numbers)
    average = positive_sum / positive_count
    median = statistics.median(positive_numbers)

    return positive_count, average, maximum, minimum, median