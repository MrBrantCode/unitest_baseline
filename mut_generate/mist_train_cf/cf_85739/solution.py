"""
QUESTION:
Design a function `process_data` that takes a list of daily stock prices for a year and returns the median share value after removing outliers and handling missing data. Outliers are defined as share values in the 1st or 99th percentile. Missing data should be replaced with the mean of the remaining values. The function should be efficient for large datasets.
"""

import numpy as np
import pandas as pd

def process_data(data):
    data_frame = pd.DataFrame(data, columns=['Share Values'])
    data_frame['Share Values'].fillna(data_frame['Share Values'].mean(), inplace=True)
    
    q_low = data_frame['Share Values'].quantile(0.01)
    q_hi = data_frame['Share Values'].quantile(0.99)
    
    data_frame_filtered = data_frame[(data_frame['Share Values'] > q_low) & (data_frame['Share Values'] < q_hi)]
    
    return data_frame_filtered['Share Values'].median()