"""
QUESTION:
Write a function called `calculate_total_sales` that takes a pandas DataFrame `df` as input, calculates the total sales for each product by multiplying `Quantity` and `UnitPrice`, and returns a new DataFrame with unique product names and their corresponding total sales. The function should not modify the original DataFrame.
"""

import pandas as pd

def calculate_total_sales(df):
    # Calculate the total sales for each product
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    # Create a new DataFrame with unique product names and their total sales
    total_sales_df = df.groupby('ProductName')['TotalPrice'].sum().reset_index()
    total_sales_df.columns = ['ProductName', 'TotalSales']
    
    return total_sales_df