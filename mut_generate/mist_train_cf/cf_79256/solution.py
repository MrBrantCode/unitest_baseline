"""
QUESTION:
Write a function `drop_highly_correlated_columns` that takes a Pandas DataFrame `df` as input, drops all columns containing missing values, and then drops columns whose absolute correlation coefficient with any other column exceeds 0.85 using the Pearson method. The function should modify the original DataFrame and return it.
"""

import pandas as pd
import numpy as np

def drop_highly_correlated_columns(df):
    # Drop columns containing missing values
    df.dropna(axis=1, inplace=True)

    corr_matrix = df.corr().abs()

    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    to_drop = [column for column in upper.columns if any(upper[column] > 0.85)]

    df.drop(df[to_drop], axis=1, inplace=True)
    return df