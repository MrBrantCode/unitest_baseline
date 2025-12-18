"""
QUESTION:
Create a Python function `select_all_employees` that takes a database connection object as input and returns all rows from the `employee_records` table in a relational database using a SQL query statement. Assume that the database connection has already been established.
"""

def select_all_employees(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee_records")
    return cur.fetchall()