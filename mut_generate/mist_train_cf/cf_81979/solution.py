"""
QUESTION:
Create a function `create_table` that creates a table named 'UserData' in a SQLite database with three columns: 'id' (a unique integer primary key), 'name' (text), and 'age' (integer). The function should return a confirmation message if the table is created successfully.
"""

import sqlite3

def create_table(conn):
    """
    Creates a table named 'UserData' in a SQLite database with three columns: 'id' (a unique integer primary key), 'name' (text), and 'age' (integer).
    
    Args:
        conn (sqlite3 connection object): The connection to the SQLite database.
    
    Returns:
        str: A confirmation message if the table is created successfully.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS UserData(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
        """
    )
    return "Table created successful."