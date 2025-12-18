"""
QUESTION:
Create a function `create_and_query_table` that takes a database name, table name, and column information as input, and allows for the creation of a table in a SQL database using Python. The function should be able to create a table with the specified columns, insert data into the table, and retrieve specific information based on a given condition.

The function should use the `sqlite3` module for database operations. The table should have two columns: "name" (text) and "age" (integer). The function should be able to insert a new row with a given name and age, and retrieve all rows where the age is greater than a specified value.

Restrictions: Use the `sqlite3` module for database operations. The database should be a local SQLite database.
"""

import sqlite3

def create_and_query_table(db_name, table_name, columns, data, condition):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    # Create a cursor object
    c = conn.cursor()
    
    # Create a table
    column_str = ", ".join([f"{key} {value}" for key, value in columns.items()])
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
    ({column_str})''')

    # Insert data into the table
    c.execute(f"INSERT INTO {table_name} VALUES (?, ?)", data)
    # Commit the changes to the database
    conn.commit()

    # Query the table to retrieve specific information
    c.execute(f"SELECT * FROM {table_name} WHERE age > ?", (condition,))
    result = c.fetchall()

    # Close the connection
    conn.close()
    return result