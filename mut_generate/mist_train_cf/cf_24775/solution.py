"""
QUESTION:
Write a function, `get_high_spenders`, that joins the `Customers` and `Orders` tables on `customer_id` and returns the `customer_id` and `name` of customers with a total order value greater than $100.
"""

import pandas as pd

def get_high_spenders(customers, orders):
    """
    Returns a DataFrame with customer_id and name of customers 
    with a total order value greater than $100.

    Args:
        customers (pd.DataFrame): DataFrame with customer information.
        orders (pd.DataFrame): DataFrame with order information.

    Returns:
        pd.DataFrame: DataFrame with customer_id and name of high spenders.
    """
    # Merge the customers and orders DataFrames on customer_id
    merged_df = pd.merge(customers, orders, on='customer_id')

    # Group by customer_id and name, then calculate total order value
    total_orders = merged_df.groupby(['customer_id', 'name'])['total'].sum().reset_index()

    # Filter for customers with total order value greater than $100
    high_spenders = total_orders[total_orders['total'] > 100]

    # Return the customer_id and name of high spenders
    return high_spenders[['customer_id', 'name']]