"""
QUESTION:
Create a function `least_squares_regression` that performs least squares regression to fit a set of data points. The function should take a list of tuples representing the data points as input and return the slope (m) and y-intercept (b) of the regression line.
"""

def least_squares_regression(data_points):
    """
    This function performs least squares regression to fit a set of data points.
    
    Args:
        data_points (list of tuples): A list of tuples representing the data points.
        
    Returns:
        tuple: A tuple containing the slope (m) and y-intercept (b) of the regression line.
    """
    n = len(data_points)
    sum_x = sum(x for x, y in data_points)
    sum_y = sum(y for x, y in data_points)
    sum_xy = sum(x * y for x, y in data_points)
    sum_x_squared = sum(x ** 2 for x, y in data_points)
    
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - m * sum_x) / n
    
    return m, b