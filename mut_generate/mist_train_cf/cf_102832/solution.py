"""
QUESTION:
Write a function, `lowest_salary_employee`, that finds the employee with the lowest salary from a database table, excluding any employees whose last name starts with the letter 'S'. The function should return the entire row of the employee with the lowest salary.
"""

import sqlite3

def lowest_salary_employee(conn):
    """
    Finds the employee with the lowest salary from the employees table, 
    excluding any employees whose last name starts with the letter 'S'.

    Args:
        conn (sqlite3 connection object): Connection to the SQLite database.

    Returns:
        A tuple representing the row of the employee with the lowest salary.
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM employees
        WHERE last_name NOT LIKE 'S%'
        ORDER BY salary ASC
        LIMIT 1
    """)
    return cursor.fetchone()