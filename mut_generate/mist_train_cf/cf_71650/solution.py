"""
QUESTION:
Write a function called `calculate_total_rainfall` that calculates the total cumulative rainfall from a list of rainfall measurements and rounds the result to the nearest whole number.
"""

def calculate_total_rainfall(rainfall_measures):
    """
    Calculate the total cumulative rainfall from a list of rainfall measurements.

    Args:
        rainfall_measures (list): A list of rainfall measurements.

    Returns:
        int: The total cumulative rainfall rounded to the nearest whole number.
    """
    total_rainfall = sum(rainfall_measures)
    return round(total_rainfall)