"""
QUESTION:
Create a function named `generate_target_field` that takes a pandas DataFrame as input and returns a new DataFrame. The input DataFrame contains columns 'name', 'age', 'height', and 'weight'. The function should add a new column 'target' which is a concatenation of 'name', 'age', 'height', and 'weight' columns. The 'age' and 'height' in the 'target' column should be formatted as two-digit and three-digit numbers with leading zeros respectively, but the problem description contains inconsistent information about the formatting of 'height' and 'weight'. The function should also sort the rows in descending order based on the 'target' field.
"""

import pandas as pd

def generate_target_field(df):
    df['target'] = df['name'] + df['age'].astype(str).str.zfill(2) + df['height'].astype(str).str.zfill(3) + df['weight'].astype(str).str.zfill(3)
    return df.sort_values('target', ascending=False)