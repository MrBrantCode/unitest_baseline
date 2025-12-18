"""
QUESTION:
Create a function `sort_students_by_age` that takes a list of student dictionaries as input, where each dictionary contains a 'name' and an 'age'. The function should return a list of student names in descending order based on their age.
"""

def sort_students_by_age(students):
    return [student['name'] for student in sorted(students, key=lambda x: x['age'], reverse=True)]