"""
QUESTION:
Write a function named `get_student_records` that uses a cursor-based pagination technique to retrieve a large set of student records from a database. The function should take two parameters: `page` and `page_size`. Implement error handling to cater for any unexpected interruptions such as loss of database connectivity. Ensure the function properly closes database connections and cursors after use.
"""

import sqlite3

def get_student_records(page, page_size):
    """
    Retrieves a page of student records from the database.

    Args:
    page (int): The page number to retrieve.
    page_size (int): The number of records per page.

    Returns:
    list: A list of student records.
    """
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        offset = (page - 1) * page_size
        cursor.execute("SELECT * FROM student LIMIT ? OFFSET ?", (page_size, offset))
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records
    except Exception as e:
        print("An error occurred while fetching the records: ", e)