"""
QUESTION:
Create a function called `calculate_scorecard_points` that takes a pandas DataFrame `df` with feature levels and their corresponding Weight of Evidence (WOE) values, an intercept, coefficients for each feature, and maximum points for each feature. The function should return a DataFrame with the WOE values converted to scorecard points for each feature level, rescaled so that the maximum number of points is 50, while assigning fewer points to riskier features.

The function should assume that the WOE values are calculated using the formula: `WOE = ln(goods/bads) - ln(overall_goods/overall_bads)`, where `goods` and `bads` are the percentage of non-events and events in each group, respectively, and `overall_goods` and `overall_bads` are the overall percentage of non-events and events.

The function should also assume that the scorecard points are calculated using the formula: `score = (WOE * coefficient) + intercept`, and then rescaled so that the maximum number of points for each feature is as specified in the `max_points` dictionary.
"""

import pandas as pd
import numpy as np

def calculate_scorecard_points(df, intercept, coefficients, max_points):
    """
    Calculate scorecard points from WOE values for each feature level.

    Parameters:
    df (pandas DataFrame): DataFrame with feature levels and their corresponding WOE values.
    intercept (float): Intercept for the weight-of-evidence scorecard.
    coefficients (list): Coefficients for each feature.
    max_points (dict): Maximum number of points for each feature.

    Returns:
    pandas DataFrame: DataFrame with WOE values converted to scorecard points for each feature level.
    """

    # calculate the scorecard points for each feature level
    for i, feature in enumerate(df.columns):
        df[f'{feature}_points'] = df[feature] * coefficients[i] + intercept
        
        # rescale the points so that the maximum number of points is 50
        df[f'{feature}_points'] = df[f'{feature}_points'] / df[f'{feature}_points'].max() * max_points[feature]
    
    return df