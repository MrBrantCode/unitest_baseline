"""
QUESTION:
Write a function named `remove_duplicates` that takes a Pandas DataFrame as input and returns two DataFrames: one containing the original DataFrame with duplicates removed (keeping the first occurrence of each duplicate) and another containing the duplicate rows with their original index positions.
"""

import pandas as pd

def remove_duplicates(df):
    duplicates = df[df.duplicated(keep='first')]
    df_unique = df.drop_duplicates(keep='first')
    return df_unique, duplicates