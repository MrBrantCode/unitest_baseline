"""
QUESTION:
Write a function `calculate_rainfall_statistics` that takes a 2D list of integers representing the month and corresponding rainfall values as input, calculates the average and standard deviation of monthly rainfall, and returns the result in a Markdown table format as a string. The input list should have 12 sublists, each containing a month (1-12) and its corresponding rainfall value. The output Markdown table should have the same structure as the original dataset table and include the average and standard deviation of monthly rainfall.
"""

import numpy as np

def calculate_rainfall_statistics(rainfall):
    """
    Calculate the average and standard deviation of monthly rainfall.

    Args:
    rainfall (list): A 2D list of integers representing the month and corresponding rainfall values.

    Returns:
    str: The result in a Markdown table format as a string.
    """
    rainfall_array = np.array(rainfall)
    rainfall_values = rainfall_array[:, 1]
    average_rainfall = np.mean(rainfall_values)
    std_rainfall = np.std(rainfall_values)
    
    markdown_table = "| Month | Rainfall (inches) |\n"
    markdown_table += "|-------|------------------|\n"
    for month, rainfall in rainfall:
        markdown_table += f"| {month} | {rainfall:.1f} |\n"
    markdown_table += "|-------|------------------|\n"
    markdown_table += f"| Average | {average_rainfall:.1f} |\n"
    markdown_table += f"| Standard Deviation | {std_rainfall:.1f} |"
    
    return markdown_table