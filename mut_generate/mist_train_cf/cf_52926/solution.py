"""
QUESTION:
Write a function `apply_func_to_df` that takes a Pandas DataFrame `df`, a custom function `func`, two column names `col1` and `col2`, and an operation as input. The function should apply the custom function to the values in `col1` and `col2` of the DataFrame according to the specified operation, and add the result as a new column to the DataFrame. The custom function should handle addition, subtraction, multiplication, and division operations.
"""

import pandas as pd

def apply_func_to_df(df, func, col1, col2, operation):
    df['New_Column'] = df.apply(lambda row: func(row[col1], row[col2], operation), axis=1)
    return df