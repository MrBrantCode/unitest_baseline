"""
QUESTION:
Create a function `update_dataframe` that takes a pandas DataFrame with columns 'Name', 'Age', and 'Salary' as input. The function should add a new column 'City' with values ['New York', 'Boston', 'Los Angeles'], update the 'Name' in the first row to 'Jonathan', and return the filtered DataFrame with rows where 'Age' is greater than or equal to 30.
"""

import pandas as pd

def update_dataframe(df):
    df['City'] = ['New York', 'Boston', 'Los Angeles']
    df.iloc[0, df.columns.get_loc('Name')] = 'Jonathan'
    return df[df['Age'] >= 30]