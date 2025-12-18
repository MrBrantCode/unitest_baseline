"""
QUESTION:
Create a function `handle_missing_values` that takes a pandas DataFrame and a string representing a statistical measure ("mean", "median", "mode") as input. The function should identify the columns with missing values in the DataFrame, calculate the percentage of missing values in each of these columns, and replace the missing values with the specified statistical measure. The function should be optimized for efficiency and handle both numeric and non-numeric data types.
"""

import pandas as pd
import numpy as np

def handle_missing_values(df, replace_with="mean"):
    # identifies columns with missing values
    missing_val_count_by_column = (df.isnull().sum())
    missing_cols = missing_val_count_by_column[missing_val_count_by_column > 0]

    # report the percentage of missing values in those columns
    for col in missing_cols.index:
        missing_percentage = df[col].isnull().mean() * 100
        print(f'{col} column has {missing_percentage: .2f} percent missing values.')

    # replace the missing values with appropriate statistical value
    for col in missing_cols.index:
        if replace_with == "mean" and np.issubdtype(df[col].dtype, np.number):
            df[col].fillna(df[col].mean(), inplace=True)
        elif replace_with == "median" and np.issubdtype(df[col].dtype, np.number):
            df[col].fillna(df[col].median(), inplace=True)
        elif replace_with == "mode":
            df[col].fillna(df[col].mode()[0], inplace=True)

    return df