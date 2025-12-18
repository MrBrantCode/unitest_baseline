"""
QUESTION:
Write a function called 'calculate_quantity_sums' that takes a pandas DataFrame as input and returns the columns, number of rows, and a list of 'quantity' values. The function should handle cases where the 'quantity' column contains non-numeric values by converting them to numeric. The DataFrame has a 'quantity' column, but its data type is not specified.
"""

import pandas as pd

def calculate_quantity_sums(df):
    """
    Calculate the columns, number of rows, and a list of 'quantity' values in a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        tuple: A tuple containing a list of columns, the number of rows, and a list of 'quantity' values.
    """
    # Ensure the 'quantity' column is numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    
    # Get the columns and number of rows
    columns = df.columns.tolist()
    rows = len(df)
    
    # Get the 'quantity' values
    quantity_sums = df['quantity'].tolist()
    
    return columns, rows, quantity_sums