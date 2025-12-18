"""
QUESTION:
Write a lambda function in Python named `std_dev` that calculates the standard deviation of a given list of numbers. The function should import the math library and use it to calculate the square root of the variance. The dataset is a list of floating point numbers, and the function should return the standard deviation of the dataset.
"""

import math

# Lambda function to Calculate the mean
mean = lambda data: sum(data) / len(data)

# Lambda function to Calculate the variance
variance = lambda data: sum((xi - mean(data)) ** 2 for xi in data) / len(data)

# Lambda function to Calculate the standard deviation
def std_dev(data):
    return math.sqrt(variance(data))