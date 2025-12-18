"""
QUESTION:
Implement a function named `linear_regression` that takes in two lists of numbers, `x` and `y`, representing data points, and returns the slope and y-intercept of the linear regression line that best fits the data using the least squares method. Additionally, calculate the R-squared value to measure the strength of the relationship between the model and the data. You are not allowed to use any libraries that directly provide a linear regression function. You can only use basic mathematical and statistical functions. The input `x` and `y` will have the same length and contain at least two distinct points.
"""

def linear_regression(x, y):
    """
    Calculate the slope and y-intercept of the linear regression line 
    that best fits the data using the least squares method.
    
    Parameters:
    x (list): A list of numbers representing the x-coordinates of the data points.
    y (list): A list of numbers representing the y-coordinates of the data points.
    
    Returns:
    m (float): The slope of the linear regression line.
    b (float): The y-intercept of the linear regression line.
    r2 (float): The R-squared value, which measures the strength of the relationship between the model and the data.
    """

    def mean(nums):
        return sum(nums)/len(nums)

    def variance(nums):
        avg = mean(nums)
        return sum((xi - avg) ** 2 for xi in nums)

    def covariance(x, avg_x, y, avg_y):
        n = len(x)
        return sum((x[i] - avg_x) * (y[i] - avg_y) for i in range(n))

    avg_x = mean(x)
    avg_y = mean(y)

    m = covariance(x, avg_x, y, avg_y) / variance(x)
    b = avg_y - m * avg_x

    y_pred = [m * xi + b for xi in x]
    ss_res = sum((yi - yi_pred) ** 2 for yi, yi_pred in zip(y, y_pred))
    ss_tot = variance(y)
    r2 = 1 - ss_res/ss_tot

    return m, b, r2