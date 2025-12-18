"""
QUESTION:
Write a function `calculate_order_statistics` that takes a DataFrame as input, where each row represents an order with 'Country' and 'Amount'. The function should group the data by 'Country', calculate the total number of orders, average order amount, and maximum order amount for each country. It should then filter out any orders where the order amount is greater than $1000 and exclude any countries where the total number of orders is less than 10.
"""

import pandas as pd

def calculate_order_statistics(df):
    """
    This function calculates order statistics for each country, 
    including total number of orders, average order amount, 
    and maximum order amount, excluding orders over $1000 
    and countries with less than 10 orders.

    Parameters:
    df (pd.DataFrame): A DataFrame containing 'Country' and 'Amount' columns.

    Returns:
    pd.DataFrame: A DataFrame with the calculated statistics for each country.
    """
    
    # Group the data by Country and calculate the required statistics
    grouped_df = df.groupby('Country').agg({'Amount': ['count', 'mean', 'max']})
    grouped_df.columns = ['Total Orders', 'Average Order Amount', 'Maximum Order Amount']

    # Filter out orders where the order amount is greater than $1000
    grouped_df = grouped_df[grouped_df['Maximum Order Amount'] <= 1000]

    # Exclude countries where the total number of orders is less than 10
    grouped_df = grouped_df[grouped_df['Total Orders'] >= 10]

    return grouped_df