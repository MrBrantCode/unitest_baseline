"""
QUESTION:
Create a function `get_sorted_customers` that connects to a SQLite database, retrieves the name, age, and address of all customers from the 'customer' table, sorts the results by age in ascending order, and returns the sorted list of customers. The function should take the database filename as a string and return a list of tuples, where each tuple contains the name, age, and address of a customer.
"""

import sqlite3

def get_sorted_customers(db_filename):
    """
    Connects to a SQLite database, retrieves the name, age, and address of all customers 
    from the 'customer' table, sorts the results by age in ascending order, and returns 
    the sorted list of customers.

    Args:
        db_filename (str): The filename of the SQLite database.

    Returns:
        list: A list of tuples, where each tuple contains the name, age, and address of a customer.
    """
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute('SELECT name, age, address FROM customer ORDER BY age ASC')
    rows = cursor.fetchall()
    conn.close()
    return rows