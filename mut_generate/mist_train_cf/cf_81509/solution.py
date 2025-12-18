"""
QUESTION:
Construct a function `normalize` in Python that normalizes the data in a pandas DataFrame by scaling it to a range of 0 to 1. The function should take a pandas DataFrame as input and return a new DataFrame with the normalized data. The function should also handle potential exceptions during the normalization process and return `None` in case of an error.
"""

import pandas as pd

def normalize(df):
    # handle potential exceptions
    try:
        result = df.copy()
        for feature_name in df.columns:
            # calculate the max and min value of each column
            max_value = df[feature_name].max()
            min_value = df[feature_name].min()
            # normalize the data to range from 0 to 1
            result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
        return result
    except Exception as e:
        print(f"There was a problem normalizing the data: {e}")
        return None