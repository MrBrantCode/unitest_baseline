"""
QUESTION:
Write a function called `sort_students` that takes a list of tuples as input, where each tuple contains a student's name, score, and age. The function should return a new list of tuples, sorted in descending order by score, and for students with the same score, sorted in ascending order by age.
"""

def sort_students(students):
    students.sort(key=lambda x: (-x[1], x[2]))
    return students