"""
QUESTION:
Create a function named `evaluate_regressor` that takes in a trained regression model (`regressor`), a feature matrix of test data (`X_test`), and actual target values of the test data (`y_test`). The function should predict the target values for `X_test` using the `regressor`, calculate the root mean squared percentage error (RMSPE) of the predictions using the formula RMSPE = sqrt(mean(((y_test - y_pred) / y_test)**2)), and return the predicted values, actual values, and the RMSPE.
"""

import numpy as np

def evaluate_regressor(regressor, X_test, y_test):
    y_pred = regressor.predict(X_test)
    rmspe = np.sqrt(np.mean(((y_test - y_pred) / y_test) ** 2))
    return y_pred, y_test, rmspe