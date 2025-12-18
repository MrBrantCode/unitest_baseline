"""
QUESTION:
Create a function named `process_dataframe` that takes a pandas DataFrame as input, performs the following operations for each row, and returns the modified DataFrame:
- Prints the index of the current row.
- Prints the values of all columns in the current row.
- Calculates the sum of all numerical values in the current row.
- Checks if any missing values exist in the current row and prints a message indicating their presence.
- Adds a new column named "Sum of Values" to store the sum calculated for each row.
- Adds a new column named "Missing Values" to store a boolean value indicating whether any missing values exist in each row.

The function should not take any arguments other than the DataFrame.
"""

import pandas as pd
import numpy as np

def process_dataframe(df):
    # Initialize the new columns
    df['Sum of Values'] = 0
    df['Missing Values'] = False

    # Iterate through each row
    for index, row in df.iterrows():
        print('Current index:', index)
        print('Values in current row:')
        print(row)
        
        # Calculate the sum of all numerical values
        sum_values = pd.to_numeric(row, errors='coerce').sum()
        print('Sum of values in current row:', sum_values)
        
        # Check for missing values
        if row.isnull().values.any():
            print('Missing values exist in current row')
            df.at[index, 'Missing Values'] = True
        else:
            df.at[index, 'Missing Values'] = False
        
        # Store the sum in the 'Sum of Values' column
        df.at[index, 'Sum of Values'] = sum_values
        
        print('------')
    
    return df