"""
QUESTION:
Implement a function `compute_r_squared` that takes two parameters: `data` and `predictions`, both lists of the same length representing original and predicted data points, respectively. The function should calculate the coefficient of determination (R^2) using the formula R^2 = 1 - (SS_res / SS_tot) where SS_res is the sum of squared residuals and SS_tot is the total sum of squares. The function should not use any external libraries and should return the calculated R^2 value.
"""

def compute_r_squared(data, predictions):
    # Calculate the mean of the original data points
    mean_data = sum(data) / len(data)
    
    # Calculate the sum of squared residuals (SS_res)
    ss_res = sum((data[i] - predictions[i]) ** 2 for i in range(len(data)))
    
    # Calculate the total sum of squares (SS_tot)
    ss_tot = sum((data[i] - mean_data) ** 2 for i in range(len(data)))
    
    # Calculate the coefficient of determination (R^2)
    r_squared = 1 - (ss_res / ss_tot)
    
    return r_squared