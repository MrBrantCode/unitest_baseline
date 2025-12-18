"""
QUESTION:
Write a function `calculate_mean_squared_error` that calculates the Mean Squared Error (MSE) for a univariate model given a list of observed values `y` and a constant `β_0`. The MSE is calculated as 1/(2N) \sum (y_n - β_0)^2, where N is the number of observations.
"""

def calculate_mean_squared_error(y, β_0):
    """
    Calculate the Mean Squared Error (MSE) for a univariate model.

    Parameters:
    y (list): A list of observed values.
    β_0 (float): A constant.

    Returns:
    float: The Mean Squared Error (MSE).
    """
    n = len(y)
    return (1 / (2 * n)) * sum((y_i - β_0) ** 2 for y_i in y)