"""
QUESTION:
Write a function `calculate_rainfall_statistics` that takes a 2D list `rainfall_data` of months and corresponding rainfall values as input, calculates the average and standard deviation of monthly rainfall, and returns the result in a Markdown table format string. The input list is expected to have 12 sublists, each containing a month (1-12) and its corresponding rainfall value.
"""

import numpy as np

def calculate_rainfall_statistics(rainfall_data):
    """
    Calculate the average and standard deviation of monthly rainfall.

    Args:
        rainfall_data (list): A 2D list of months and corresponding rainfall values.

    Returns:
        str: A Markdown table format string containing the average and standard deviation of monthly rainfall.
    """
    rainfall_array = np.array(rainfall_data)
    rainfall_values = rainfall_array[:, 1]
    average_rainfall = np.mean(rainfall_values)
    std_rainfall = np.std(rainfall_values)

    result = "| Month | Rainfall (inches) |\n"
    result += "|-------|------------------|\n"
    for month, rainfall in rainfall_data:
        result += f"| {month} | {rainfall:.1f} |\n"
    result += "|-------|------------------|\n"
    result += f"| Average | {average_rainfall:.1f} |\n"
    result += f"| Standard Deviation | {std_rainfall:.1f} |\n"
    return result