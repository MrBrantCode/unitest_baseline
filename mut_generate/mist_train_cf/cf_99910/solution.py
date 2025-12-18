"""
QUESTION:
Write a function `calculate_rainfall_statistics` that takes a 2D list `rainfall` as input where each sublist contains a month (integer) and corresponding rainfall (float) value. The function should calculate the average and standard deviation of the rainfall values, and return the result as a Markdown table format string with the same structure as the original dataset table, including the average and standard deviation at the end.
"""

import numpy as np

def calculate_rainfall_statistics(rainfall):
    """
    Calculate the average and standard deviation of rainfall values from a given 2D list.

    Args:
    rainfall (list): A 2D list where each sublist contains a month (integer) and corresponding rainfall (float) value.

    Returns:
    str: A Markdown table format string with the same structure as the original dataset table, including the average and standard deviation at the end.
    """
    rainfall_array = np.array(rainfall)
    rainfall_values = rainfall_array[:, 1]
    average_rainfall = np.mean(rainfall_values)
    std_rainfall = np.std(rainfall_values)
    
    table = "| Month | Rainfall (inches) |\n"
    table += "|-------|------------------|\n"
    for month, rainfall in rainfall:
        table += f"| {month} | {rainfall:.1f} |\n"
    table += "|-------|------------------|\n"
    table += f"| Average | {average_rainfall:.1f} |\n"
    table += f"| Standard Deviation | {std_rainfall:.1f} |"
    
    return table