"""
QUESTION:
Write a Python function, `filter_students`, that takes a list of dictionaries representing students, each containing 'name' and 'age' keys, and returns a new list of students sorted in ascending order by name. The function should filter out students whose age is below 18 and include only those whose name starts with the letter 'A'.
"""

def filter_students(students):
    return sorted(
        [
            student
            for student in students
            if student['age'] >= 18 and student['name'].startswith('A')
        ],
        key=lambda student: student['name']
    )