"""
QUESTION:
Filter a Pandas DataFrame to include only rows where a specific column's values are present in a given list.

Create a function named `filter_dataframe` that takes a Pandas DataFrame `df` and a list `my_list` as input, and returns a new DataFrame containing only the rows where the values in the column 'class' are present in `my_list`. The function should not modify the original DataFrame.
"""

import pandas as pd

def filter_dataframe(df, my_list):
    return df[df['class'].isin(my_list)]