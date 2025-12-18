"""
QUESTION:
Write a function `best_fit_line` that takes a list of points as input, where each point is a tuple of two numbers (x, y), and returns the slope (m) and y-intercept (b) of the best-fit line for the given points. The function should use O(1) memory complexity.
"""

def best_fit_line(data):
    """
    This function calculates the slope (m) and y-intercept (b) of the best-fit line 
    for the given points in O(1) memory complexity.

    Args:
        data (list): A list of points where each point is a tuple of two numbers (x, y)

    Returns:
        tuple: A tuple containing the slope (m) and y-intercept (b) of the best-fit line
    """
    # Initialize variables for the sums
    n = len(data)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_squared = 0

    # Calculate the sums
    for x, y in data:
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x_squared += x ** 2

    # Calculate the slope and y-intercept
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - m * sum_x) / n

    return m, b