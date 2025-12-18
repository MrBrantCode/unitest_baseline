"""
QUESTION:
Implement a function named `pivot_table` that takes a DataFrame and two column names as input, and returns a new DataFrame with the specified columns as index and columns. The function should also handle missing values and support advanced aggregation methods.

The function should be able to efficiently handle large datasets, be versatile and user-friendly, and provide options to customize its behavior. It should also allow specifying a value to replace missing values in the result and support specifying a function or a list of functions to apply during aggregation.
"""

import pandas as pd
import numpy as np

def pivot_table(df, index, columns, aggfunc='mean', fill_value=None):
    """
    Creates a spreadsheet-style pivot table as a DataFrame.

    Parameters:
    df (DataFrame): DataFrame to create the pivot table from.
    index (str or list of str): Column name(s) to use as index.
    columns (str or list of str): Column name(s) to use as columns.
    aggfunc (str or list of str, optional): Function(s) to apply during aggregation.
        Defaults to 'mean'.
    fill_value (scalar, optional): Value to replace missing values in the result.
        Defaults to None.

    Returns:
    DataFrame: The resulting pivot table.
    """
    return pd.pivot_table(df, index=index, columns=columns, aggfunc=aggfunc, fill_value=fill_value)