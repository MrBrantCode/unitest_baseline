"""
QUESTION:
Implement a method `transform_data` that takes a 2D NumPy array `XY` as input. The method should create an array `X` by stacking a column of ones and all but the last column of `XY`, and an array `Y` containing the last column of `XY`. The output arrays `X` and `Y` should be stored as instance variables. The input array `XY` is not empty and contains at least two columns.
"""

import numpy as np

def transform_data(XY):
    X_intercept = np.ones(len(XY))  # Create an array filled with the value 1
    X = np.column_stack((X_intercept, XY[:, :-1]))  # Stack X_intercept and all but the last column of XY
    Y = XY[:, -1]  # Extract the last column of XY and store it as Y
    return X, Y