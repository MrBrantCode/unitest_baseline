"""
QUESTION:
Create a function `select_products` to select all rows from a table named 'products' that have a price less than 10 and a quantity greater than 5. The function should return the rows in descending order of the product's price. The function should interact with an SQLite database.
"""

import sqlite3

def select_products(conn):
    """
    Select all rows from 'products' table where price < 10 and quantity > 5.
    The rows are returned in descending order of the product's price.

    Args:
        conn (sqlite3.Connection): Connection to the SQLite database.

    Returns:
        list: A list of tuples, where each tuple represents a row in the 'products' table.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price < 10 AND quantity > 5 ORDER BY price DESC")
    return cursor.fetchall()