"""
QUESTION:
Implement a function `least_squares(x_values, y_values)` that takes two lists of numbers `x_values` and `y_values` as input, representing the dataset for linear regression. The function should return the slope and y-intercept of the best fitting line according to the least squares method, as well as the mean squared error (MSE) of the predicted and actual y_values. The implementation should only use basic Python, without any external libraries like Numpy or Scipy.
"""

def least_squares(x_values, y_values):
    # Compute the sums needed to solve linear regression 
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_x2 = sum([i**2 for i in x_values])
    sum_xy = sum([i*j for i, j in zip(x_values, y_values)])

    # Calculate number of observations
    n = len(x_values)
    
    # Calculate the parameters of the best fitting line
    denominator = n*sum_x2 - sum_x**2
    a = (n*sum_xy - sum_x*sum_y) / denominator
    b = (sum_y*sum_x2 - sum_x*sum_xy) / denominator

    # Calculate the predicted values
    y_preds = [a*x + b for x in x_values]

    # Calculate the mean squared error
    mse = sum([(i-j)**2 for i, j in zip(y_values, y_preds)]) / n

    return a, b, mse