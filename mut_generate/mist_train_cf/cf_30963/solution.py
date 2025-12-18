"""
QUESTION:
Implement a function `compute_trajectory_features_set1` that takes four parameters: 
- `aligned_trajector_key_file`: a pandas DataFrame containing aligned trajectory key data,
- `parameters`: a dictionary containing parameters for feature computation,
- `start_time`: the start time for computing trajectory features,
- `end_time`: the end time for computing trajectory features.
The function should compute trajectory features based on the provided parameters and time range, and return a new pandas DataFrame `features_df` populated with the computed features.
"""

import pandas as pd
from typing import Dict

def compute_trajectory_features_set1(aligned_trajector_key_file: pd.DataFrame, parameters: Dict, start_time, end_time):
    features_df = pd.DataFrame()

    # Compute trajectory features based on parameters and time range
    features_df['feature1'] = aligned_trajector_key_file['trajectory_data1'] * parameters['param1']
    features_df['feature2'] = aligned_trajector_key_file['trajectory_data2'] + parameters['param2']
    features_df['feature3'] = (end_time - start_time) * parameters['param3']

    return features_df