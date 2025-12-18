"""
QUESTION:
Implement a function `calculate_standard_deviation` that takes a list of numbers as input and returns the standard deviation of the data set. The function should calculate the standard deviation using the formula: σ = sqrt(1/N * Σ(xi - μ)^2), where σ is the standard deviation, N is the number of data points, xi is the i-th data point, and μ is the mean of the data set.
"""

import math
import statistics

def calculate_standard_deviation(numbers):
    n = len(numbers)
    mean = statistics.mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_deviation = math.sqrt(variance)
    return std_deviation