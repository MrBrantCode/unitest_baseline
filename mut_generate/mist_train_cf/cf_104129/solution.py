"""
QUESTION:
Write a query to filter data from the "inventory" table based on the following conditions: 
- Include only items with a quantity greater than 10.
- Include only items located in either "Warehouse A" or "Warehouse B".
- Order the results by the "last_updated" column in descending order.
"""

import pandas as pd

def filter_inventory(df):
    """
    Filter inventory data based on quantity, location, and last updated date.

    Args:
    df (pd.DataFrame): Inventory data.

    Returns:
    pd.DataFrame: Filtered inventory data.
    """
    return df[(df['quantity'] > 10) & (df['location'].isin(["Warehouse A", "Warehouse B"]))].sort_values(by='last_updated', ascending=False)