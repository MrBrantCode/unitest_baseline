"""
QUESTION:
Implement a function named `calculate_mse` that calculates the Mean Squared Error (MSE) in a single-variable model. The function should take as input a list of observed values `y` and a list of predicted values `beta_0`. The function should return the MSE as a float value, with the formula being 1/(2N) * ∑ (y_n - β_0)^2, where N is the number of observations.
"""

def calculate_mse(y, beta_0):
    """
    Calculate the Mean Squared Error (MSE) in a single-variable model.

    Args:
        y (list): A list of observed values.
        beta_0 (list): A list of predicted values.

    Returns:
        float: The MSE value.
    """
    N = len(y)  # Get the number of observations
    # Calculate the sum of squared differences
    sse = sum((y_n - b0) ** 2 for y_n, b0 in zip(y, beta_0))
    # Calculate the MSE
    mse = (1 / (2 * N)) * sse
    return mse