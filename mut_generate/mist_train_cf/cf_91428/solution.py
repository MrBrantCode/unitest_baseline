"""
QUESTION:
Create a function called `insert_new_row` that takes in `itemname`, `quantity`, and `price` as parameters. This function should connect to a SQLite database, check if a table named 'Inventory' exists and create it if not. The function must validate that `itemname` is a non-empty string, `quantity` is a positive integer, and `price` is a positive decimal number. If validation passes, it should insert a new row into the 'Inventory' table with the provided details. The function should close the database connection after execution. Assume the database connection details are provided and necessary database library is imported.
"""

import sqlite3

def insert_new_row(itemname, quantity, price):
    # Connect to the database
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Check if the Inventory table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Inventory'")
    table_exists = cursor.fetchone()
    if not table_exists:
        # Create the table if it doesn't exist
        cursor.execute("CREATE TABLE Inventory (id INTEGER PRIMARY KEY AUTOINCREMENT, itemname TEXT, quantity INTEGER, price REAL)")

    # Validate the input values
    if not isinstance(itemname, str) or not itemname:
        print("Invalid itemname")
        conn.close()
        return
    if not isinstance(quantity, int) or quantity <= 0:
        print("Invalid quantity")
        conn.close()
        return
    if not isinstance(price, (int, float)) or price <= 0.0:
        print("Invalid price")
        conn.close()
        return

    # Insert a new row into the Inventory table
    cursor.execute("INSERT INTO Inventory (itemname, quantity, price) VALUES (?, ?, ?)", (itemname, quantity, price))
    conn.commit()

    # Close the database connection
    conn.close()