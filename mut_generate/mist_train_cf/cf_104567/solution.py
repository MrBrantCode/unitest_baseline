"""
QUESTION:
Calculate the mean, median, and mode of a data set. The data set will always contain at least 5 elements and may contain negative numbers. Create a function called `calculate_statistics` that takes a list of numbers as input and prints the mean, median, and mode of the data set.
"""

from statistics import mean, median, mode

def calculate_statistics(data):
    """
    This function calculates and returns the mean, median, and mode of a given data set.

    Args:
        data (list): A list of numbers.

    Returns:
        tuple: A tuple containing the mean, median, and mode of the data set.
    """

    # Calculate the mean of the data set
    data_mean = mean(data)

    # Calculate the median of the data set
    data_median = median(data)

    # Try to calculate the mode of the data set
    try:
        data_mode = mode(data)
    except StatisticsError:
        data_mode = "not applicable"

    return data_mean, data_median, data_mode