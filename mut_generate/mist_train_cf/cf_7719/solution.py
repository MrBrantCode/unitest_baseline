"""
QUESTION:
Write a function `sort_students` that takes a list of dictionaries as input, where each dictionary contains a student's name, age, and grade. Sort the list in descending order of grade, then by name (to handle multiple students with the same name), then in ascending order of age for students with different names, and in descending order of age for students with the same name. Return the sorted list of dictionaries.
"""

def sort_students(students):
    students.sort(key=lambda x: (-x['grade'], x['name'], -x['age']))
    return students