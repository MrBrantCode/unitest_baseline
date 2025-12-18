"""
QUESTION:
Write a SQL query that retrieves the top 5 employees from the "employees" table with the highest salaries, including their department names and job titles, along with the average salary for each department. The result set should be ordered in descending order by salary.
"""

import sqlite3

def top_employees(conn):
    cursor = conn.cursor()
    query = """
    SELECT e.employee_name, e.job_title, e.salary, d.department_name, AVG(e.salary) as average_salary
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    GROUP BY e.employee_name, e.job_title, e.salary, d.department_name
    ORDER BY e.salary DESC
    LIMIT 5
    """
    cursor.execute(query)
    return cursor.fetchall()