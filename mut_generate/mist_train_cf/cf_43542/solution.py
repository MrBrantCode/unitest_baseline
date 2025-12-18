"""
QUESTION:
Create a function named `drop_columns_with_nulls` that takes a Pandas DataFrame as input and returns a new DataFrame with all columns containing missing or null values removed.
"""

def drop_columns_with_nulls(df):
    return df.dropna(axis=1)