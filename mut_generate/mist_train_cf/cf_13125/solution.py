"""
QUESTION:
Write a function `filter_rows` that takes a Pandas DataFrame and a threshold value as input, and returns a new DataFrame. The function should also accept an optional parameter to specify the column to compute the mean for. The new DataFrame should only contain the rows where the value in the specified column (or the mean of the row if no column is specified) is greater than the given threshold.
"""

import pandas as pd

def filter_rows(dataframe, threshold, column=None):
    if column is None:
        mean = dataframe.mean(axis=1)
    else:
        mean = dataframe[column]
    return dataframe[mean > threshold]