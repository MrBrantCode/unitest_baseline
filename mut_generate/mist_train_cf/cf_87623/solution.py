"""
QUESTION:
Create a function `get_product_sales` that takes a database connection and table name as input. The function should return a pandas DataFrame containing the name of the product, the location of the store, the country of the store, and the total sales for each product. The DataFrame should only include products with a price greater than 100 and belonging to a store located in a country starting with the letter "A". The function should handle the database connection internally.
"""

import pandas as pd
import sqlite3

def get_product_sales(conn, table_name):
    """
    Retrieves product sales data from a SQLite database.
    
    Parameters:
    conn (sqlite3.Connection): A connection to the SQLite database.
    table_name (str): The name of the table to query.
    
    Returns:
    pd.DataFrame: A DataFrame containing the product name, store location, country, and total sales.
    """
    query = f"""
    SELECT ProductName, StoreLocation, Country, SUM(Sales) as TotalSales
    FROM {table_name}
    WHERE Price > 100 AND Country LIKE 'A%'
    GROUP BY ProductName, StoreLocation, Country
    """
    df = pd.read_sql_query(query, conn)
    return df