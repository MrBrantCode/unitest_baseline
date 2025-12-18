"""
QUESTION:
Write a function to retrieve job titles from a table of employees. The function should return a list of distinct job titles, sorted in descending order by the average salary of employees with each title. The function should exclude any job titles with less than 10 employees or an average salary less than $50,000.
"""

def job_titles(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT job_title
        FROM employees
        GROUP BY job_title
        HAVING COUNT(*) >= 10 AND AVG(salary) >= 50000
        ORDER BY AVG(salary) DESC
    """)
    return [row[0] for row in cur.fetchall()]