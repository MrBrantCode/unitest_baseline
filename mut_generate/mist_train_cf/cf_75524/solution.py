"""
QUESTION:
Create a function `get_full_results` that takes a fitted `GridSearchCV` object as input and returns a pandas DataFrame containing the comprehensive results of the grid search, sorted by `mean_fit_time`. The function should utilize the `cv_results_` attribute of the `GridSearchCV` object to obtain the results.
"""

import pandas as pd

def get_full_results(GridSearch_fitted):
    """
    Returns a pandas DataFrame containing the comprehensive results of the grid search,
    sorted by mean_fit_time.

    Parameters:
    GridSearch_fitted (GridSearchCV): A fitted GridSearchCV object.

    Returns:
    pandas DataFrame: Comprehensive results of the grid search.
    """
    full_results = pd.DataFrame(GridSearch_fitted.cv_results_)
    full_results = full_results.sort_values(by=['mean_fit_time'])
    return full_results