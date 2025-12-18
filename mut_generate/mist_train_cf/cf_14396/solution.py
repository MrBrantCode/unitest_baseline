"""
QUESTION:
Create a function `filter_rows` that takes a pandas DataFrame `df` and a column name `column` as input, and returns a new DataFrame. The function should drop rows with missing values in the specified `column`, then filter the remaining rows to include only those where the 'Age' is greater than 20, and finally sort the resulting rows in descending alphabetical order by 'Name'.
"""

import pandas as pd

def filter_rows(df, column):
    # Drop rows with missing values in specified column
    df = df.dropna(subset=[column])
    
    # Filter rows where Age > 20 and Name is alphabetically ordered in descending order
    df = df[(df['Age'] > 20)].sort_values('Name', ascending=False)
    
    return df