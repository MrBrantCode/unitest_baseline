"""
QUESTION:
Implement the `sort_features_by_priority` function that takes in the following parameters:
- `features`: a list of feature names
- `prev_importance_df`: a DataFrame containing the previous feature importance computation with an 'importance' column
- `using_prev_fit_fi`: a list of feature names for which importance computation was done using a previous fit model

The `sort_features_by_priority` function should sort the features by priority based on their importance computation, handling the mix of current and previous fit models and unevaluated features. The function should return a list of feature names sorted by priority.
"""

import pandas as pd

def sort_features_by_priority(features, prev_importance_df, using_prev_fit_fi):
    # Create a DataFrame for the current features
    curr_importance_df = prev_importance_df[~prev_importance_df.index.isin(using_prev_fit_fi)]
    
    # Sort the features by importance
    sorted_prev_fit_features = prev_importance_df[prev_importance_df.index.isin(using_prev_fit_fi)].sort_values('importance', ascending=False).index.tolist()
    sorted_curr_fit_features = curr_importance_df.sort_values('importance', ascending=False).index.tolist()
    
    # Combine the sorted features from previous and current fit models
    sorted_features = sorted_prev_fit_features + sorted_curr_fit_features
    
    return sorted_features