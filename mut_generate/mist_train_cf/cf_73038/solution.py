"""
QUESTION:
Create a function named `select_user_by_name` that takes a SQLite database connection and a username as input, and returns the user data from the 'users' table where the 'username' matches the input. 

Restrictions: 
- Use parameterized queries to prevent SQL injection attacks.
- Handle potential exceptions that may occur during database operations.
- The database connection should be properly closed after use.
"""

import sqlite3
from sqlite3 import Error

def select_user_by_name(conn, username):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
        return None