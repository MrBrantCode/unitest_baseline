"""
QUESTION:
Create a function `convert_to_sorted_list` that takes a pandas DataFrame and a column name as input, removes rows with null values in the specified column, sorts the DataFrame in descending order based on that column, and returns the sorted column values as a Python list. The function should not include any null values in the output list.
"""

import pandas as pd

def convert_to_sorted_list(df, column_name):
    df = df.dropna(subset=[column_name])
    df = df.sort_values(by=column_name, ascending=False)
    return df[column_name].tolist()