"""
QUESTION:
Write a function `calculate_rainfall_statistics` that takes a list of lists, where each sublist contains a month (integer) and rainfall (float) for that month. Calculate the average and standard deviation of the rainfall values and return the results in a Markdown table format string, including the original data, average, and standard deviation. The table should have two columns: "Month" and "Rainfall (inches)".
"""

import numpy as np

def calculate_rainfall_statistics(rainfall):
    """
    Calculate the average and standard deviation of rainfall values and return the results in a Markdown table format string.

    Args:
    rainfall (list of lists): A list of lists, where each sublist contains a month (integer) and rainfall (float) for that month.

    Returns:
    str: A Markdown table format string, including the original data, average, and standard deviation.
    """
    # convert the dataset to a numpy array
    rainfall_array = np.array(rainfall)
    # extract the rainfall values
    rainfall_values = rainfall_array[:, 1]
    # calculate the average monthly rainfall
    average_rainfall = np.mean(rainfall_values)
    # calculate the standard deviation of monthly rainfall
    std_rainfall = np.std(rainfall_values)

    # generate the Markdown table format string
    result = "| Month | Rainfall (inches) |\n"
    result += "|-------|------------------|\n"
    for month, rainfall in rainfall:
        result += f"| {month} | {rainfall:.1f} |\n"
    result += "|-------|------------------|\n"
    result += f"| Average | {average_rainfall:.1f} |\n"
    result += f"| Standard Deviation | {std_rainfall:.1f} |\n"

    return result