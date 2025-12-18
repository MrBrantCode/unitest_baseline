"""
QUESTION:
Write a Python function `select_entry_by_id` that extracts a specific entry from a SQLite database by ID and manages potential anomalies. The function should take a database connection `conn` and an entry ID `id` as parameters. It should execute an SQL query to select the entry with the specified ID from a table, and return the entry. The database connection and query execution should be handled to avoid potential anomalies and ensure uniformity of the data.
"""

import sqlite3
from sqlite3 import Error

def select_entry_by_id(conn, id):
    """
    Extracts a specific entry from a SQLite database by ID.

    Args:
        conn (sqlite3.Connection): The SQLite database connection.
        id (int): The ID of the entry to be extracted.

    Returns:
        tuple: The extracted entry.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name WHERE id=?", (id,))
    return cursor.fetchone()