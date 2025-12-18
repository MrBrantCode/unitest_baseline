"""
QUESTION:
Create a function `find_unique_positive_numbers` that takes no arguments. The function should return the average of unique positive numbers in the 'quantity' column from the database table 'Orders', rounded to two decimal places, and the count of these unique positive numbers. Exclude any negative numbers or null values from the result set.
"""

import pandas as pd

def find_unique_positive_numbers(df):
    """
    This function calculates the average of unique positive numbers in the 'quantity' column 
    from the given DataFrame and returns the average and the count of these unique positive numbers.

    Parameters:
    df (pd.DataFrame): A pandas DataFrame containing the 'Orders' table.

    Returns:
    tuple: A tuple containing the average of unique positive numbers and their count.
    """
    # Filter the DataFrame to include only positive numbers and remove duplicates
    unique_positive_numbers = df['quantity'].dropna()[df['quantity'] > 0].unique()
    
    # Calculate the average of unique positive numbers
    average = round(unique_positive_numbers.mean(), 2)
    
    # Get the count of unique positive numbers
    count = len(unique_positive_numbers)
    
    return average, count