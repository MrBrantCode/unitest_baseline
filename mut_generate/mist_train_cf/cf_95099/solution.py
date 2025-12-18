"""
QUESTION:
Create a function `generate_target_field` that takes a pandas DataFrame with columns 'name', 'age', and 'height' as input, and returns the DataFrame with an additional 'target' column. The 'target' column should be a concatenation of the 'name', 'age', and 'height' columns, where 'age' and 'height' are formatted as two-digit and three-digit numbers with leading zeros respectively.
"""

import pandas as pd

def generate_target_field(df):
    return df.assign(target=df.apply(lambda row: row['name'] + str(row['age']).zfill(2) + str(row['height']).zfill(3), axis=1))