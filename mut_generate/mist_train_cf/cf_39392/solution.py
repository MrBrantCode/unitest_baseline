"""
QUESTION:
Implement the `calculate_covariance` method in the `Statistics` class to calculate the covariance between two sets of data, `data1` and `data2`, using the formula `cov(X, Y) = Σ((X[i] - μX) * (Y[i] - μY)) / n`. The `calculate_covariance` method should take no arguments, and the class has a `calculate_mean(data)` method that calculates the mean of a given set of data. The `data1` and `data2` attributes are lists of data points.
"""

def calculate_covariance(data1, data2):
    n = len(data1)
    mean_data1 = sum(data1) / len(data1)
    mean_data2 = sum(data2) / len(data2)
    covariance = sum((data1[i] - mean_data1) * (data2[i] - mean_data2) for i in range(n)) / n
    return covariance