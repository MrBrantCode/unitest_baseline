"""
QUESTION:
Implement a function `calculate_true_labels` that takes in two parameters: `testing_data` (a 2D NumPy array of shape (n_samples, n_features)) and `pred` (a 2D NumPy array of shape (n_samples, n_classes)). The function should return a 1D NumPy array `y_true` of shape (n_samples), where each element is the index of the column with the maximum predicted value in the corresponding row of `pred`.
"""

import numpy as np

def calculate_true_labels(testing_data, pred):
    return np.argmax(pred, axis=1)