"""
QUESTION:
Write a function named `select_rows_and_columns` that takes a Pandas DataFrame as input and returns a new DataFrame with specific rows and columns selected based on the following conditions: 'Age' greater than 30 and 'City' either 'Paris' or 'Tokyo', and only include the 'Name' and 'Salary' columns.
"""

import pandas as pd

def select_rows_and_columns(df):
    return df.loc[(df['Age'] > 30) & ((df['City'] == 'Paris') | (df['City'] == 'Tokyo')), ['Name', 'Salary']]