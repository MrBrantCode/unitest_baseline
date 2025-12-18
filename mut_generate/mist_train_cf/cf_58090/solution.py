"""
QUESTION:
Given a pandas DataFrame `X` and an instance of `RFE` (`selector`) that has been fitted to `X` and a target variable `y`, extract the column names of the selected features from `X` using the `support_` attribute of `selector`. The `support_` attribute is a boolean array where `True` indicates that the feature was selected. Implement a function `get_selected_features` that returns the selected column names as a numpy array or a list. The function should take `X` and `selector` as input.
"""

import numpy as np

def get_selected_features(X, selector):
    """
    Extract the column names of the selected features from X using the support_ attribute of selector.
    
    Parameters:
    X (pandas DataFrame): DataFrame containing features.
    selector (RFE): An instance of RFE that has been fitted to X and a target variable y.
    
    Returns:
    numpy array: A numpy array of the selected column names.
    """
    return np.array(X.columns)[selector.support_]