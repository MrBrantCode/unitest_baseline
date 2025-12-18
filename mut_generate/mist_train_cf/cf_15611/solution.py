"""
QUESTION:
Create a function named `create_dataframe` that takes a dictionary of lists as input, where the keys represent column names and the values represent column values. Convert the column names to uppercase and the column values in the 'Sales' column to numeric (they are not strings as shown in the provided answer). Remove any duplicate values from the 'Sales' column and sort the resulting DataFrame in descending order based on the 'Sales' column.
"""

import pandas as pd

def create_dataframe(data):
    df = pd.DataFrame(data)
    df.columns = df.columns.str.upper()  # convert column names to uppercase
    df['SALES'] = pd.to_numeric(df['SALES'])  # convert 'Sales' column to numeric
    df = df.drop_duplicates(subset='SALES')  # remove duplicate values
    df = df.sort_values(by='SALES', ascending=False)  # sort by 'Sales' column in descending order
    return df