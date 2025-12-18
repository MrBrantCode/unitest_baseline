"""
QUESTION:
Create a function named `generate_target_field` that takes a Pandas DataFrame as input. The DataFrame contains the columns 'name', 'age', and 'height'. The function should return the input DataFrame with a new column 'target' added. The 'target' column is a concatenation of the 'name', 'age', and 'height' columns, where 'age' and 'height' are formatted as two-digit and three-digit numbers with leading zeros, respectively.
"""

import pandas as pd

def generate_target_field(df):
    df['target'] = df.apply(lambda row: row['name'] + str(row['age']).zfill(2) + str(row['height']).zfill(3), axis=1)
    return df