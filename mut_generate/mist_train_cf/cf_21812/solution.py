"""
QUESTION:
Write a function `percentile_calculator` that takes a list of numbers as input and returns a tuple containing the median and the 99th percentile of the input data. The function should be designed to be used in a MapReduce framework, with a custom combiner to optimize the intermediate data transmission and reduce network traffic.
"""

import numpy as np

def percentile_calculator(data):
    """
    Calculate the median and 99th percentile of the input data.

    Args:
        data (list): A list of numbers.

    Returns:
        tuple: A tuple containing the median and the 99th percentile of the input data.
    """
    # Sort the list of data points
    sorted_data = sorted(data)

    # Calculate the median
    median = np.median(sorted_data)

    # Find the index of the 99th percentile
    percentile_index = int(len(sorted_data) * 0.99)

    # Calculate the 99th percentile
    percentile = sorted_data[percentile_index]

    # Return the median and 99th percentile as a tuple
    return (median, percentile)