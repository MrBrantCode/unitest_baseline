"""
QUESTION:
Create a function `create_dataframe` that takes a pandas DataFrame as input. The function should return a new DataFrame where each value in the 'text1' and 'text2' columns is 20 characters or less, excludes any rows with 'NaN' values, and ensures that the values in 'text1' and 'text2' columns do not overlap with each other. The function should also split the 'text' column into 'text1' and 'text2' columns with equal distribution.
"""

import pandas as pd

def create_dataframe(df):
    # Remove rows with NaN values
    df = df.dropna()

    # Split the 'text' column into 'text1' and 'text2' columns with equal distribution
    df[['text1', 'text2']] = df['text'].str.split(n=1, expand=True)

    # Truncate 'text1' and 'text2' columns to 20 characters
    df['text1'] = df['text1'].str.slice(stop=20)
    df['text2'] = df['text2'].str.slice(stop=20)

    return df