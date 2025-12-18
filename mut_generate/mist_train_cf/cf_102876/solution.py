"""
QUESTION:
Write a function `calculate_mean_median_mode` that takes a list of numbers as input and returns the mean, median, and mode of the list. The mean is calculated by summing up all the values in the list and dividing it by the total number of values. The median is the middle value of a sorted list. If the list has an even number of values, the median is the average of the two middle values. The mode is the value that appears most frequently in the list. If no value appears more than once, the function should return `None` for the mode.
"""

from statistics import mode
from statistics import StatisticsError

def calculate_mean_median_mode(data_set):
    # Mean
    mean = sum(data_set) / len(data_set)

    # Median
    sorted_data_set = sorted(data_set)
    if len(sorted_data_set) % 2 == 0:
        median = (sorted_data_set[len(sorted_data_set) // 2] + sorted_data_set[len(sorted_data_set) // 2 - 1]) / 2
    else:
        median = sorted_data_set[len(sorted_data_set) // 2]

    # Mode
    try:
        mode_value = mode(data_set)
    except StatisticsError:
        mode_value = None

    return mean, median, mode_value