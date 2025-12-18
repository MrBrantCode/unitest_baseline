"""
QUESTION:
Write a function `calculate_variance` to compute the variance of a given list of historical return data using Bessel's correction. The function should take a list of numbers as input and return the variance of the data. Assume the input list contains at least two numbers.
"""

def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return variance