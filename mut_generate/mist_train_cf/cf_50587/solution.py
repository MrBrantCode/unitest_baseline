"""
QUESTION:
Write a function `series_to_dataframe` that takes a pandas Series of numpy arrays as input and returns a DataFrame. The DataFrame should have a column 'name' containing the index values of the Series and columns 0 to n-1 containing the corresponding numpy array values, where n is the length of the numpy arrays. The function should work for a Series with any number of rows and any length of numpy arrays.
"""

import pandas as pd

def series_to_dataframe(series):
    return pd.DataFrame(series.tolist(), index=series.index).reset_index().rename(columns={'index': 'name'})