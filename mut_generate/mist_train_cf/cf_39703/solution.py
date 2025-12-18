"""
QUESTION:
Implement a function `custom_r2_score` that takes two lists of numbers, `y_true` and `y_pred`, as input and returns the R-squared value calculated using the formula:

\[ R^2 = 1 - \frac{\sum_{i=1}^{n}(y_{true,i} - y_{pred,i})^2}{\sum_{i=1}^{n}(y_{true,i} - \bar{y}_{true})^2} \]

where `n` is the number of observations, `y_true,i` and `y_pred,i` are the true and predicted values for the `i-th` observation, and `\bar{y}_{true}` is the mean of the true values.
"""

def custom_r2_score(y_true, y_pred):
    n = len(y_true)
    mean_y_true = sum(y_true) / n
    sum_squared_residuals = sum((y_true[i] - y_pred[i])**2 for i in range(n))
    sum_squared_total = sum((y_true[i] - mean_y_true)**2 for i in range(n))
    r_squared = 1 - (sum_squared_residuals / sum_squared_total)
    return r_squared