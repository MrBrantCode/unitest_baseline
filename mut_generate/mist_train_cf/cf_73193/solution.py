"""
QUESTION:
Create a function called mean_squared_error that calculates the mean squared error between actual and predicted values in a univariate model. The actual values are represented by y, the predicted values are represented by a constant coefficient β_0 (the intercept of the regression line), and the function should include a factor of 1/2 for computational convenience. The input to the function should be a list of actual values y and the coefficient β_0, and the output should be the mean squared error.
"""

def mean_squared_error(y, beta_0):
    """
    This function calculates the mean squared error between actual and predicted values in a univariate model.
    
    Parameters:
    y (list): A list of actual values
    beta_0 (float): The intercept of the regression line
    
    Returns:
    float: The mean squared error
    """
    # Calculate the sum of squared differences
    sum_squared_diff = sum((actual - beta_0) ** 2 for actual in y)
    
    # Calculate the mean squared error with a factor of 1/2 for computational convenience
    mse = sum_squared_diff / (2 * len(y))
    
    return mse