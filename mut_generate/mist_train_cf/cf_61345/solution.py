"""
QUESTION:
Write a function named `average_temperature` that calculates the average temperature from a given list of temperature values. The function should take a list of numbers as input and return the average temperature. The input list is not empty and contains only numbers.
"""

def average_temperature(data):
    """
    Calculate the average temperature from a given list of temperature values.

    Args:
        data (list): A list of temperature values.

    Returns:
        float: The average temperature.
    """
    return sum(data) / len(data)