"""
QUESTION:
Write a function named `group_orders` that takes a Pandas DataFrame `df` as input. The DataFrame contains columns 'Order ID', 'Country', 'Order Type', and 'Quantity'. The function should group the DataFrame by 'Country' and 'Order Type', calculate the total quantity of each 'Order Type' per 'Country', and return the resulting DataFrame with 'Country', 'Order Type', and 'Total_Quantity' columns.
"""

import pandas as pd

def group_orders(df):
    return df.groupby(['Country', 'Order Type'])[['Quantity']].sum().reset_index()