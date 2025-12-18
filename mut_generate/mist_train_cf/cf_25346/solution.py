"""
QUESTION:
Write a Python function `get_students_over_18` that takes a list of student dictionaries as input, where each dictionary represents a student with 'name' and 'age' keys. Return a list of names of students who are older than 18. The input list may contain any number of student dictionaries.
"""

def get_students_over_18(students):
    return [student['name'] for student in students if student['age'] > 18]