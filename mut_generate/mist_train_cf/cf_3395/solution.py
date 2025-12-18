"""
QUESTION:
Write a function named `sort_students` that takes a list of tuples as input. Each tuple contains a student name, their score, and their age. The function should return a new list of tuples with the students sorted in descending order based on their scores. If multiple students have the same score, they should be sorted in ascending order based on their ages.
"""

def sort_students(students):
    # Sort students based on scores in descending order and ages in ascending order
    students.sort(key=lambda x: (-x[1], x[2]))
    return students