"""
QUESTION:
Create a Python function, `AcademiaDatabase`, to design and manage a database for storing and retrieving academic data of students in an educational institution. The database should have two tables: one for general student information (id and name) and another for academic specifics (id and grade). The function should be able to create these tables, insert data into them, and retrieve all student names and grades. Implement this using SQLite database system in Python.
"""

import sqlite3

def AcademiaDatabase(db_name):
  conn = sqlite3.connect(db_name)
  cursor = conn.cursor()

  # Create table for general students' info
  cursor.execute('''CREATE TABLE students
                     (id INT PRIMARY KEY, name TEXT)''')

  # Create table for students' academic specifics
  cursor.execute('''CREATE TABLE academic
                     (id INT PRIMARY KEY, grade REAL, FOREIGN KEY(id) REFERENCES students(id))''')

  def insert_student(id, name):
    cursor.execute("INSERT INTO students VALUES (?,?)", (id, name))
    conn.commit()

  def insert_academic(id, grade):
    cursor.execute("INSERT INTO academic VALUES (?,?)", (id, grade))
    conn.commit()

  def retrieve_all():
    cursor.execute("SELECT students.name, academic.grade FROM students INNER JOIN academic ON students.id = academic.id")
    return cursor.fetchall()

  return insert_student, insert_academic, retrieve_all