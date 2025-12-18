"""
QUESTION:
Implement a Python function called "calculate_total_cost" that takes an order ID as input and returns the total cost of the order by joining the "orders" table with the "products" table on the "Product_Name" column. The function should multiply the quantity of each product by its unit price from the "products" table, handle cases where the given order ID does not exist in the "orders" table or where the corresponding product name does not exist in the "products" table, and return an error message for such cases. The function should assume that the "products" table already exists with the necessary data.
"""

import pandas as pd

def calculate_total_cost(order_id, orders, products):
    """
    Calculate the total cost of an order by joining the orders table with the products table.

    Args:
    order_id (int): The ID of the order.
    orders (pd.DataFrame): The orders table.
    products (pd.DataFrame): The products table.

    Returns:
    float: The total cost of the order. If the order ID does not exist or a product is not found, returns an error message.
    """
    # Filter the orders table by the given order ID
    order = orders[orders['Order_ID'] == order_id]
    
    # If the order ID does not exist, return an error message
    if order.empty:
        return "Error: Order ID not found."

    # Merge the orders table with the products table on the Product_Name column
    merged_table = pd.merge(order, products, on='Product_Name')

    # If a product is not found, return an error message
    if merged_table['Unit_Price'].isnull().any():
        return "Error: Product not found."

    # Calculate the total cost by multiplying the quantity of each product by its unit price
    total_cost = (merged_table['Quantity'] * merged_table['Unit_Price']).sum()

    return total_cost