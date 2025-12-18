"""
QUESTION:
Write a function `process_dataframe(df)` that takes a pandas DataFrame as input and performs the following operations:
- Iterates over each row in the DataFrame, printing the index and values of the row.
- Calculates the sum of numerical values in the row and creates a new column "Sum of Values" to store this sum.
- Checks for missing values in the row, prints a message if found, and creates a new column "Missing Values" to store a boolean indicating the presence of missing values.
- If the sum of numerical values exceeds 100, prints a message.
- Removes rows with missing values.
- Removes rows with non-numeric values.
- Sorts the DataFrame by the "Sum of Values" column in descending order.
- Returns the processed DataFrame.

Restrictions:
- The function should handle DataFrames with any number and names of columns.
- The function should handle both numerical and missing values in the DataFrame.
"""

import pandas as pd

def process_dataframe(df):
    sum_column = []
    missing_values_column = []
    for index, row in df.iterrows():
        print(f"Row index: {index}")
        print(f"Row values: {row.values}")
        
        numeric_values = [val for val in row.values if pd.api.types.is_numeric_dtype(type(val)) or (isinstance(val, float) and not pd.isnull(val))]
        row_sum = sum(numeric_values)
        sum_column.append(row_sum)
        
        missing_values = any(pd.isnull(row))
        missing_values_column.append(missing_values)
        
        if missing_values:
            print("Missing values detected in this row.")
            continue
        
        if row_sum > 100:
            print("Sum of values exceeds the limit.")
    
    df['Sum of Values'] = sum_column
    df['Missing Values'] = missing_values_column
    
    df = df.dropna()
    df = df.apply(pd.to_numeric, errors='coerce').dropna()
    df = df.sort_values(by='Sum of Values', ascending=False)
    
    return df