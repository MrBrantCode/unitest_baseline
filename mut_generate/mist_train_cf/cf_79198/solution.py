"""
QUESTION:
Create a Python function named `create_connection` to establish a connection to a SQLite database and return the connection object. This function should handle potential errors and print relevant messages.
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'successful connection with {db_file}')
    except Error as e:
        print(e)
    finally:
        return conn