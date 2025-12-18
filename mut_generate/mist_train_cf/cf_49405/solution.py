"""
QUESTION:
Write a function `calculate_skewness(data)` that calculates the skewness of a given list of numbers without using any external libraries. The function should take a list of numbers as input and return the skewness value. The skewness should be calculated using the formula `Skew[X] = E[( (X - μ)/σ )^3]` where `μ` is the Mean, `σ` is the Standard Deviation, and `E` is the Expectation operation.
"""

def calculate_skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    skewness = sum((x - mean) ** 3 for x in data) * n / ((n - 1) * (n - 2) * std_dev ** 3)
    return skewness