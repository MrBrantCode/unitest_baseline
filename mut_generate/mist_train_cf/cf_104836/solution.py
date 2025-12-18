"""
QUESTION:
Write a function named `find_students` that retrieves the name, age, and grade of students. The function should return the results for students whose age is greater than 18, who are in grade 12 or higher, and whose last name starts with the letter "S".
"""

def find_students(students):
    return [student for student in students if student['age'] > 18 and student['grade'] >= 12 and student['last_name'].startswith('S')]