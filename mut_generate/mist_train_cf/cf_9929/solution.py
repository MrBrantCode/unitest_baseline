"""
QUESTION:
Write a function `get_customer_details` to retrieve customer details along with their total number of orders and the average order value from a database containing `customer` and `orders` tables. The function should join the tables based on `customer_id` and return the results grouped by `customer_id` and `customer_name`.
"""

import pandas as pd

def get_customer_details(customer, orders):
    """
    Retrieve customer details along with their total number of orders and the average order value.

    Parameters:
    customer (DataFrame): DataFrame containing customer information.
    orders (DataFrame): DataFrame containing order information.

    Returns:
    DataFrame: A DataFrame containing customer details, total orders, and average order value.
    """
    
    # Merge the customer and orders DataFrames based on customer_id
    merged_df = pd.merge(customer, orders, on='customer_id', how='left')
    
    # Group the merged DataFrame by customer_id and customer_name, and calculate total orders and average order value
    result_df = merged_df.groupby(['customer_id', 'customer_name']).agg({
        'order_id': 'count',
        'order_value': 'mean'
    }).reset_index()
    
    # Rename the columns for better readability
    result_df.columns = ['customer_id', 'customer_name', 'total_orders', 'average_order_value']
    
    return result_df