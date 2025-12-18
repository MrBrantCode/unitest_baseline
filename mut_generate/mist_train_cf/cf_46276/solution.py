"""
QUESTION:
Implement a function `calculate_metrics` that takes a month name and a list of average daily temperatures for that month as input and returns the month name along with the average, variance, and standard deviation of the temperatures (rounded to 2 decimal places). The variance is the average of the squared deviations from the mean, and the standard deviation is the square root of the variance.
"""

import math

def calculate_metrics(month, temperatures):
    n = len(temperatures)
    mean = sum(temperatures) / n
    variance = sum((xi - mean) ** 2 for xi in temperatures) / n
    standard_deviation = math.sqrt(variance)
    return month, round(mean, 2), round(variance, 2), round(standard_deviation, 2)