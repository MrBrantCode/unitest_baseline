"""
QUESTION:
Write a function called `calculate_average_temperature` that takes a list of seven temperatures representing a seven-day forecast as input. Calculate and return the average temperature of the entire forecast, not just today's temperature. The function should be able to handle a list of integers representing temperatures.
"""

def calculate_average_temperature(forecast):
    return sum(forecast) / len(forecast)