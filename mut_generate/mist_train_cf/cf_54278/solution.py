"""
QUESTION:
Write a function called `calculate_sse` that takes in two parameters: `x` (a list of x-coordinates of the data points), and `y` (a list of y-coordinates of the data points), `m` (the gradient of the line of best fit), and `c` (the y-intercept of the line of best fit). The function should return the Sum of Squared Errors (SSE) between the data points and the line of best fit defined by `m` and `c`.
"""

def calculate_sse(x, y, m, c):
    """
    Calculate the Sum of Squared Errors (SSE) between data points and a line of best fit.

    Args:
    x (list): A list of x-coordinates of the data points.
    y (list): A list of y-coordinates of the data points.
    m (float): The gradient of the line of best fit.
    c (float): The y-intercept of the line of best fit.

    Returns:
    float: The Sum of Squared Errors (SSE) between the data points and the line of best fit.
    """
    return sum((yi - (m * xi + c)) ** 2 for xi, yi in zip(x, y))