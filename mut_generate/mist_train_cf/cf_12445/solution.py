"""
QUESTION:
Implement a `simple_linear_regression` function in Python that takes in two lists `x` and `y` representing the years of experience and corresponding salaries of employees, and returns the slope and intercept of the simple linear regression line calculated using the least squares method. The function should not include any input/output operations or data visualization. The input lists `x` and `y` are assumed to be valid, containing only non-negative integers, and having the same length.
"""

def simple_linear_regression(x, y):
    """
    Calculate the slope and intercept of a simple linear regression line.

    Args:
    x (list): A list of years of experience.
    y (list): A list of corresponding salaries.

    Returns:
    tuple: A tuple containing the slope and intercept of the regression line.
    """
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([xi*yi for xi, yi in zip(x, y)])
    sum_x2 = sum([xi**2 for xi in x])

    slope = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    intercept = (sum_y - slope*sum_x) / n

    return slope, intercept