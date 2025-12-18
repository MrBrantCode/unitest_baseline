"""
QUESTION:
Implement a function named `calculate_r_squared` that computes the coefficient of determination (R-squared) between two numerical datasets. The function should take two lists of numbers `x` and `y` as input and return the R-squared value. The function should handle potential exceptions or edge cases, such as division by zero and unequal lengths of input lists.

Additionally, implement a function named `split_data` that splits a given list of numbers into training and testing sets based on a specified ratio. The function should take a list of numbers `data` and an optional ratio `ratio` as input, and return the training and testing sets.

Both functions should be implemented without using any external libraries, except for the `math` module for the square root calculation.
"""

import math

def calculate_r_squared(x, y):
    assert len(x) == len(y), "Lengths of x and y must be equal"
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(i*i for i in x)
    sum_y_sq = sum(i*i for i in y)
    sum_xy = sum(i*j for i, j in zip(x, y))
    denominator = math.sqrt((n * sum_x_sq - sum_x**2) * (n * sum_y_sq - sum_y**2))
    if denominator == 0:
        return 0
    else:
        return (n * sum_xy - sum_x * sum_y) / denominator

def split_data(data, ratio=0.8):
    train_size = int(len(data) * ratio)
    train_set = data[:train_size]
    test_set = data[train_size:]
    return train_set, test_set