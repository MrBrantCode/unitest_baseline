"""
QUESTION:
Create a function named `fill_with_most_frequent` that takes a Pandas DataFrame as input and returns the DataFrame with missing values filled with the most frequent value from each column. If there is more than one most frequent value, the function should randomly select one of them. The function should handle missing values efficiently by iterating over each column.
"""

import pandas as pd
import numpy as np

def fill_with_most_frequent(df):
    most_frequent_values = df.mode().iloc[0]
    most_frequent_dict = most_frequent_values.to_dict()
    
    for column in df.columns:
        df[column].fillna(most_frequent_dict[column], inplace=True)
        
    return df