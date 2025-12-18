"""
QUESTION:
Write a Python function `prevent_sql_injection` that takes a user input and a query as input and returns the query result while preventing SQL injection attacks. The function should use parameterized queries to minimize the risk of SQL injection. 

Assume that a SQLite database named 'my_database.db' with a table named 'users' and a column named 'id' already exists.
"""

import sqlite3

def prevent_sql_injection(user_input):
    """
    This function prevents SQL injection attacks by using parameterized queries.

    Args:
        user_input (str): The input from the user.

    Returns:
        list: A list of rows from the query result.
    """
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (user_input,))
    result = c.fetchall()
    conn.close()
    return result