"""
QUESTION:
Create a function called `initialize_db` that initializes a relational database management system. The function should take one parameter `db_file`, which is the name of the database file. The function should establish a connection to the database, create two tables (`Table1` and `Table2`) with a foreign key constraint between them to ensure data normalization, and handle any errors that occur during the process. The function should be designed to run in a separate thread.
"""

import sqlite3
from sqlite3 import Error

def initialize_db(db_file):
    """
    Initializes a relational database management system.
    
    Parameters:
    db_file (str): The name of the database file.
    
    Returns:
    None
    """
    sql_create_table1 = """ CREATE TABLE IF NOT EXISTS Table1 (
                        id integer PRIMARY KEY,
                        name text NOT NULL,
                        description text
                    ); """
    sql_create_table2 = """ CREATE TABLE IF NOT EXISTS Table2 (
                        id integer PRIMARY KEY,
                        name text NOT NULL,
                        description text,
                        table1_id integer,
                        FOREIGN KEY (table1_id) REFERENCES Table1 (id)
                    ); """

    # Establishing a connection to the DB
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        return

    # Creating tables
    try:
        conn.execute(sql_create_table1)
        conn.execute(sql_create_table2)
    except Error as e:
        print(e)