"""
QUESTION:
Implement a function called `secure_query` that takes a database query and user input as arguments and returns the query result without allowing the user input to be directly injected into the query, preventing a blind SQL injection attack. The function should use parameterized queries or prepared statements to separate the SQL code from the user input. Assume the database is SQLite and the query is a SELECT statement.
"""

import sqlite3

def secure_query(query, user_input):
    """
    Execute a secure database query using parameterized queries to prevent blind SQL injection attacks.

    Args:
    query (str): The SQL query to execute.
    user_input (str): The user input to be used in the query.

    Returns:
    list: The result of the query execution.
    """

    # Establish a connection to the database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Execute the query with the user input as a parameter
    cursor.execute(query, (user_input,))

    # Fetch all results from the query execution
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    return results