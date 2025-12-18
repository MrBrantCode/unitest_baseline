"""
QUESTION:
Create a function named `select_rows` that takes a pandas DataFrame as input and returns a new DataFrame containing only the rows where the 'name' column is not empty and the 'age' column has a value greater than 30.
"""

import pandas as pd

def select_rows(df):
    return df[df['name'].notnull() & (df['age'] > 30)]