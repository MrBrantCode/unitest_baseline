"""
QUESTION:
Implement the `handle_missing_values` function that takes in two input arrays, `y` and `X`, and handles missing values in the time-series data. The function should handle missing values in both `y` and `X` if `X` is provided, and only in `y` if `X` is not provided. The function should return the endogenous array with missing values handled and the exogenous array with missing values handled, if applicable. The input arrays can contain NaN (Not a Number) values representing missing values.
"""

import numpy as np

def handle_missing_values(y, X=None):
    """
    Handle missing values in the input arrays.

    Parameters:
    y : array-like or None, shape=(n_samples,)
        The endogenous (time-series) array.
    X : array-like or None, shape=(n_samples, n_features), optional
        The exogenous (feature) array.

    Returns:
    y_handled : array-like, shape=(n_samples,)
        The endogenous array with missing values handled.
    X_handled : array-like, shape=(n_samples, n_features)
        The exogenous array with missing values handled, if X is not None.
    """

    if X is not None:
        y_handled = np.nan_to_num(y)
        X_handled = np.nan_to_num(X)
    else:
        y_handled = np.nan_to_num(y)
        X_handled = None

    return y_handled, X_handled