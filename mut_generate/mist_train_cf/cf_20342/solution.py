"""
QUESTION:
Filter a DataFrame using multiple OR conditions in Pandas with case-insensitive filtering. 

Create a function named `filter_dataframe_or_conditions` that takes a DataFrame and a list of conditions as input, and returns the filtered DataFrame. The function should optimize for time complexity and ensure case-insensitive filtering. The DataFrame will contain a column named 'col1' with string values, and the conditions will be a list of strings.
"""

import pandas as pd

def filter_dataframe_or_conditions(df, conditions):
    return df[df['col1'].str.contains('|'.join(conditions), case=False, regex=True)]