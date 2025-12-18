"""
QUESTION:
Write a function named `handle_null_values` that handles null values in a given Pandas DataFrame. The function should fill null values in numerical columns (int64 and float64) with the median, and fill null values in categorical columns (object type) with the most common category (mode). Additionally, write a function named `report_null_values` that reports the percentage of null values for each column in the dataset. Both functions should be efficient enough to handle large datasets.
"""

import pandas as pd
import numpy as np

def handle_null_values(df):
    for column in df.columns:
        if df[column].dtype == 'object':  # Categorical data
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].median(), inplace=True)
    return df

def report_null_values(df):
    report = {col: (np.sum(df[col].isnull()) / df.shape[0]) * 100 for col in df.columns}
    return report