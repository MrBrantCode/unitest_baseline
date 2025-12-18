"""
QUESTION:
Create a function `convert_woe_to_scorecard` that takes in a pandas DataFrame `df` with WOE values for each feature level, the intercept of the weight-of-evidence scorecard, and a list of coefficients corresponding to each feature. The function should return a new DataFrame with the scorecard points for each feature level. The scorecard points should be calculated using the formula `(WOE * coefficient) + intercept`. The function should also ensure that the maximum number of scorecard points assigned to any feature is 50, and assign points to each feature based on the given point allocation (e.g., 30 points to feature A, 40 points to feature B, and 30 points to feature C).
"""

import pandas as pd
import numpy as np

def convert_woe_to_scorecard(df, intercept, coefficients, max_points):
    """
    Convert WOE values to scorecard points for each feature level.

    Parameters:
    df (pandas DataFrame): DataFrame with WOE values for each feature level.
    intercept (float): Intercept of the weight-of-evidence scorecard.
    coefficients (list): List of coefficients corresponding to each feature.
    max_points (dict): Dictionary of maximum points for each feature.

    Returns:
    pandas DataFrame: DataFrame with scorecard points for each feature level.
    """
    for feature in df.columns:
        # Calculate scorecard points for each feature level
        df[f'{feature}_points'] = df[feature] * coefficients[df.columns.tolist().index(feature)] + intercept
        
        # Rescale points so that the maximum number of points is 50
        df[f'{feature}_points'] = df[f'{feature}_points'] / df[f'{feature}_points'].max() * max_points[feature]
        
        # Ensure the maximum number of scorecard points assigned to any feature is 50
        df[f'{feature}_points'] = df[f'{feature}_points'].apply(lambda x: min(x, 50))
    
    return df