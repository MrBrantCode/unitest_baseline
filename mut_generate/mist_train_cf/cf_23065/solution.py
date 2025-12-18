"""
QUESTION:
Write a SQL query for the 'Orders' table to find the count of unique positive numbers in the 'quantity' column and the average of these positive numbers, excluding negative numbers. The query should return two values: the count of unique positive numbers and the average of the positive numbers.
"""

import sqlite3

def find_unique_and_average_positive_numbers(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(DISTINCT quantity) AS count_unique_numbers, AVG(quantity) AS average_positive_numbers FROM Orders WHERE quantity > 0")
    result = cur.fetchone()
    conn.close()
    return result