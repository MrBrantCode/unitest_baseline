"""
QUESTION:
Create a function `filter_rows_by_value_columns` that filters rows in a given DataFrame. The function should return a new DataFrame containing only rows where the absolute value of all columns whose names start with 'Value' is less than 1. The number of 'Value' columns in the DataFrame is unknown but is greater than 0.
"""

def filter_rows_by_value_columns(df):
    return df[df.filter(like='Value').abs().max(axis=1) < 1]