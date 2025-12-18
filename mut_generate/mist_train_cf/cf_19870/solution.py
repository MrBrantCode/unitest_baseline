"""
QUESTION:
Implement a function named `select_rows` that takes a pandas DataFrame and returns a new DataFrame with rows where the 'name' column is not null, the 'age' column is greater than 30, and the 'salary' column is between 50000 and 100000.
"""

import pandas as pd

def select_rows(df):
    return df[(df['name'].notnull()) & 
              (df['age'] > 30) & 
              ((df['salary'] >= 50000) & (df['salary'] <= 100000))]