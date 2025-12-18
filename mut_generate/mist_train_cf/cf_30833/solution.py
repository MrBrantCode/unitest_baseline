"""
QUESTION:
Write a function `analyze_basketball_data(df)` that takes a pandas DataFrame `df` with columns 'name', 'height', 'weight', 'avg', 'avg_category', and 'handedness' as input. The function should return a tuple of two DataFrames: 
1. A DataFrame containing the sum of all numerical columns (excluding 'name' and 'avg') for each combination of 'avg_category' and 'handedness'.
2. A DataFrame containing the sum of all numerical columns (excluding 'name', 'avg', and 'handedness') for each 'avg_category'.

The function should handle missing or inconsistent data gracefully.
"""

import pandas as pd

def analyze_basketball_data(df):
    # Grouping by 'avg_category' and 'handedness', and calculating the sum of numerical columns
    df_grouped_by_avg_handedness = df[['height', 'weight', 'avg_category', 'handedness']].groupby(by=['avg_category', 'handedness']).sum().reset_index()
    
    # Grouping by 'avg_category' and calculating the sum of numerical columns
    df_grouped_by_avg = df[['height', 'weight', 'avg_category']].groupby(by=['avg_category']).sum()
    
    return df_grouped_by_avg_handedness, df_grouped_by_avg