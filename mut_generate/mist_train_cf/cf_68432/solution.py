"""
QUESTION:
Create two functions in Python to manage records in a SQLite database table named "contacts" with a primary key "contact_id". 

Function 1: check_record_existence
- Returns True if a record with a given id exists in the "contacts" table; False otherwise.
- Parameters: database connection object, contact id.
- Should handle exceptions and have proper error messages in case of failure.

Function 2: update_status_if_exists
- If the record exists (using Function 1), updates the status of that record to 'inactive'. 
- If the record doesn't exist, returns an error message.
- Parameters: database connection object, contact id, new status.
- Should handle exceptions and have proper error messages in case of failure.
"""

import sqlite3
from sqlite3 import Error

def check_record_existence(conn, id):
    try:
        cur = conn.cursor()
        query = "SELECT * FROM contacts WHERE contact_id = ?"
        cur.execute(query, (id,))

        return bool(cur.fetchone())
    except Error as e:
        print(f"An error occurred: {e}")
        return False

def update_status_if_exists(conn, id, new_status):
    if check_record_existence(conn, id):
        try:
            cur = conn.cursor()
            query = "UPDATE contacts SET status = ? WHERE contact_id = ?"
            cur.execute(query, (new_status, id))

            print(f"Status of contact with id: {id} - was updated to {new_status}")
        except Error as e:
            print(f"An error occurred: {e}")
    else:
        return "Record does not exist."