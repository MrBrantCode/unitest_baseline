"""
QUESTION:
Create a function named `calculate_params` that establishes a logarithmic model 'y = a * ln(x) + b' to a dataset and returns the values of parameters 'a' and 'b'. The function should use the least squares method and take two lists of float numbers, `x_data` and `y_data`, as input where `x_data` represents the x-values and `y_data` represents the corresponding y-values of the dataset.

Note that `x_data` should not contain any zeros, as logarithm of zero is undefined. 

The function should not use any external libraries for curve fitting.
"""

import math

def calculate_params(x_data, y_data):
    """
    Establish a logarithmic model 'y = a * ln(x) + b' to a dataset using the least squares method.

    Args:
        x_data (list): A list of float numbers representing the x-values of the dataset.
        y_data (list): A list of float numbers representing the corresponding y-values of the dataset.

    Returns:
        tuple: A tuple containing the values of parameters 'a' and 'b' in the logarithmic model.

    Note:
        x_data should not contain any zeros, as logarithm of zero is undefined.
    """
    n = len(x_data)
    sum_x = sum(math.log(x) for x in x_data)
    avg_x = sum_x / n
    avg_y = sum(y_data) / n
    diff_product_sum = sum(math.log(x_data[i]) * (y_data[i] - avg_y) for i in range(n))
    diff_square_sum = sum((math.log(x_data[i]) - avg_x)**2 for i in range(n))
    a = diff_product_sum / diff_square_sum
    b = avg_y - a * avg_x
    return a, b