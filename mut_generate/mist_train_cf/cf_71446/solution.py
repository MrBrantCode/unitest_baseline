"""
QUESTION:
Implement a function `ridge_regression(X, y, lambda_)` that performs Ridge regression from scratch on the given dataset. The function should take as input the feature matrix `X`, target vector `y`, and regularization parameter `lambda_`. The function should return the coefficients of the linear model. The implementation should include feature scaling, adding a bias term, and regularization. 

The function should be evaluated using 10-fold cross-validation and the performance should be compared to the Scikit-learn Ridge regression implementation. Additionally, investigate how the regularization parameter influences the performance of the model by plotting the average root-mean-square error against the regularization parameter. 

Assume that the necessary libraries are installed and available.
"""

import numpy as np

def ridge_regression(X, y, lambda_):
    m, n = X.shape
    I = np.eye(n)
    theta = np.linalg.inv(X.T @ X + lambda_ * I) @ X.T @ y
    return theta