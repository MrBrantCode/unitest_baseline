"""
QUESTION:
Write a function `calculate_range_statistics` that takes two integers `start` and `end` as input and calculates the sum, product, average, maximum, minimum, and standard deviation of the numbers in the range from `start` to `end` (inclusive). The function should return a dictionary containing the calculated statistics.
"""

import math

def calculate_range_statistics(start, end):
    """
    Calculate the sum, product, average, maximum, minimum, and standard deviation of the numbers in the range from start to end (inclusive).

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        dict: A dictionary containing the calculated statistics.
    """

    total_sum = 0
    product = 1
    count = 0
    max_num = float('-inf')
    min_num = float('inf')
    squares = []

    for num in range(start, end+1):
        total_sum += num
        product *= num
        count += 1
        squares.append(num**2)

        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    average = total_sum / count
    sum_of_squares = sum(squares)
    variance = (sum_of_squares / count) - (average**2)
    standard_deviation = math.sqrt(variance)

    return {
        "sum": total_sum,
        "product": product,
        "average": average,
        "max": max_num,
        "min": min_num,
        "standard_deviation": standard_deviation
    }