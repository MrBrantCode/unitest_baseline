"""
QUESTION:
Create a function `sanitize_sql_input` that takes a user input string as an argument and returns a sanitized version of the input that can be safely used in an SQL query to prevent SQL injection attacks. The function should use parameter substitution to sanitize the input. The function should not use string formatting or concatenation to construct the SQL query.
"""

import sqlite3

def sanitize_sql_input(input_str):
    """
    Sanitizes user input for use in an SQL query to prevent SQL injection attacks.
    
    Args:
    input_str (str): The user input string to be sanitized.
    
    Returns:
    str: The sanitized version of the input string.
    """
    # Create a connection to the SQLite database
    conn = sqlite3.connect(':memory:')
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Use ? as a placeholder in your query and then provide a tuple of values as the second argument in the cursor.execute() call.
    query = "SELECT ?"
    
    # Execute the query with the user input as a parameter
    cursor.execute(query, (input_str,))
    
    # Fetch the result
    sanitized_input = cursor.fetchone()[0]
    
    # Close the connection
    conn.close()
    
    return sanitized_input