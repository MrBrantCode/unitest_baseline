"""
QUESTION:
Write a function called `group_by_region_and_compute_mean` that takes a list of dictionaries as input where each dictionary contains 'name', 'region', and 'score' keys. Group the input data by the 'region' key and compute the mean 'score' for each region. The function should return the mean scores for each region. The input data is in the following format: [{'name': str, 'region': str, 'score': float}, ...].
"""

import pandas as pd

def group_by_region_and_compute_mean(data):
    df = pd.DataFrame(data)
    return df.groupby('region')['score'].mean()