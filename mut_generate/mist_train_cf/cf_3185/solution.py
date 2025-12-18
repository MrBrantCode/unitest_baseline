"""
QUESTION:
Create a function named `calculate_statistics` that takes a list of numbers as input and returns the sum, median, mode, and range of the numbers. The sum should be accurate to two decimal places. The median is the middle value of the list when sorted in ascending order. If the list has an even number of values, the median is the average of the two middle values. The mode is the value that appears most frequently in the list. If multiple values have the same maximum frequency, all of them should be considered as modes. The range is the difference between the maximum and minimum values. The list can contain any number of positive, negative, or zero numbers, which can be integers or floating-point numbers, and can be in any order.
"""

import statistics
from collections import Counter

def calculate_statistics(numbers):
    sum_of_numbers = sum(numbers)
    median_value = statistics.median(numbers)
    mode_values = [num for num, freq in Counter(numbers).items() if freq == max(Counter(numbers).values())]
    range_value = max(numbers) - min(numbers)
    return round(sum_of_numbers, 2), median_value, mode_values, round(range_value, 2)