"""
QUESTION:
Write a function named `calculate_mse` that calculates the Mean Squared Error (MSE) for a single-parameter model. The function should take two parameters: a list of actual output values `y` and the model parameter `β0`. The function should return the calculated MSE value.
"""

def calculate_mse(y, β0):
    """
    Calculate the Mean Squared Error (MSE) for a single-parameter model.

    Args:
    y (list): A list of actual output values.
    β0 (float): The model parameter.

    Returns:
    float: The calculated MSE value.
    """
    return sum((yi - β0) ** 2 for yi in y) / (2 * len(y))