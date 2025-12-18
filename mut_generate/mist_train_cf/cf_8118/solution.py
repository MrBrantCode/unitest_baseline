"""
QUESTION:
Construct a function named `process_dataframe` that takes a Pandas DataFrame `df` as input and performs the following operations:
- Iterate through each row of the DataFrame in reverse order.
- For each row, calculate the sum of all numerical values and check for missing values.
- If a row contains missing values, remove it from the DataFrame.
- If a row contains non-numerical values, skip it.
- If the sum of numerical values exceeds 1000, terminate the loop.
- Create two new columns, "Sum of Values" of float data type and "Missing Values" of boolean data type, and populate them accordingly.
- Print a message if the sum exceeds 100.
- Sort the DataFrame by the "Sum of Values" column in descending order and return it.

The input DataFrame must contain at least 10 rows and 5 columns with column names of at least 5 characters each, both numerical and non-numerical values, and at least one row with missing values and one row with non-numerical values.
"""

import pandas as pd

def process_dataframe(df):
    """
    Process a DataFrame by removing rows with missing values, skipping non-numerical rows, 
    and terminating if the sum of numerical values exceeds 1000. Then, it creates two new 
    columns, "Sum of Values" and "Missing Values", and sorts the DataFrame by "Sum of Values" 
    in descending order.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The processed DataFrame.
    """

    # Reverse the dataframe
    df = df[::-1].reset_index(drop=True)

    # Initialize the "Sum of Values" and "Missing Values" columns with NaN
    df['Sum of Values'] = float('NaN')
    df['Missing Values'] = bool('NaN')

    # Loop through each row in reverse order
    for index, row in df.iterrows():
        # Calculate the sum of numerical values in the row
        num_sum = sum(value for value in row if pd.api.types.is_numeric_dtype(type(value)))

        # Check if any missing values exist
        if row.isnull().values.any():
            df.drop(index, inplace=True)
            continue

        # Check if sum exceeds the limit
        if num_sum > 1000:
            break

        # Update the "Sum of Values" column
        df.at[index, 'Sum of Values'] = num_sum

        # Update the "Missing Values" column
        df.at[index, 'Missing Values'] = row.isnull().values.any()

        # Print a message if the sum exceeds 100
        if num_sum > 100:
            print("Sum exceeds 100.")

    # Sort the dataframe based on the "Sum of Values" column in descending order
    df.sort_values(by='Sum of Values', ascending=False, inplace=True)

    return df