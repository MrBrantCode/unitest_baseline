"""
QUESTION:
Create a function `create_sales_pivot_table` that takes a Pandas DataFrame `data` as input and returns a two-way pivot table. The input DataFrame has columns 'transaction_id', 'customer_id', 'product_id', 'quantity', and 'price'. The pivot table should have 'customer_id' as the rows, 'product_id' as the columns, and the sum of 'quantity' as the values. Additionally, the pivot table should include a separate column for the total sales (sum of 'price') for each customer.
"""

import pandas as pd

def create_sales_pivot_table(data):
    pivot_table = pd.pivot_table(data, values='quantity', index='customer_id', columns='product_id', aggfunc='sum', fill_value=0)
    total_sales = data.groupby('customer_id')['price'].sum().reset_index()
    pivot_table['total_sales'] = total_sales.set_index('customer_id')['price']
    return pivot_table