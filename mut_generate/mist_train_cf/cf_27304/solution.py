"""
QUESTION:
Create a Python function `prepare_nn_input` that takes a pandas DataFrame `df` with time series data, an integer `lookback` for the number of time steps to look back, an integer `lookforward` for the number of time steps to look forward, and a list of strings `features` for the feature columns to be included in the input data. The function should return a 3D numpy array `X_res` representing the input data and a 2D numpy array `y_res` representing the target data, with dimensions (n - (lookback + lookforward), lookback + lookforward + 1, len(features)) and (n - (lookback + lookforward), 1), respectively. The function should handle time gaps in the data and prepare the input data according to the specified lookback and lookforward window.
"""

import pandas as pd
import numpy as np

def prepare_nn_input(df, lookback, lookforward, features):
    # Sort the DataFrame by the "time" column
    df.sort_values(by="time", inplace=True)
    
    # Calculate the number of time steps
    n = len(df)
    
    # Initialize arrays to store the processed input and target data
    X_res = np.zeros((n - (lookback + lookforward), lookback + lookforward + 1, len(features)))
    y_res = np.zeros((n - (lookback + lookforward), 1))
    
    # Handle time gaps in the data
    time_diff = (df["time"] - df["time"].shift(1)).fillna(0)
    time_diff = time_diff.cumsum()
    
    # Prepare the input data for the neural network
    for i in range(n - (lookback + lookforward)):
        X_res[i] = df[features].values[i:i+lookback+lookforward+1]
        y_res[i] = df[features[0]].values[i+lookback+lookforward]
    
    return X_res, y_res