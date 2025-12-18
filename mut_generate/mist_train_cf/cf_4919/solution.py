"""
QUESTION:
Write a function `calculate_statistics` that takes a list of numbers as input and returns the harmonic mean, geometric mean, and mode of the absolute values in the list. The harmonic mean is the reciprocal of the arithmetic mean of the reciprocals of the absolute values, the geometric mean is the nth root of the product of the absolute values where n is the number of elements, and the mode is the most frequent absolute value. The geometric mean should be rounded to the nearest integer.
"""

from collections import Counter
import math

def calculate_statistics(data_set):
    """
    This function calculates the harmonic mean, geometric mean, and mode of the absolute values in the input list.

    Parameters:
    data_set (list): A list of numbers.

    Returns:
    tuple: A tuple containing the harmonic mean, geometric mean, and mode of the absolute values.
    """

    # Step 1: Calculate absolute values
    abs_data_set = [abs(num) for num in data_set]

    # Step 2: Calculate harmonic mean
    harmonic_mean = len(abs_data_set) / sum(1 / num for num in abs_data_set)

    # Step 3: Calculate geometric mean
    geometric_mean = round(math.prod(abs_data_set) ** (1 / len(abs_data_set)))

    # Step 4: Calculate mode
    mode = Counter(abs_data_set).most_common(1)[0][0]

    return harmonic_mean, geometric_mean, mode