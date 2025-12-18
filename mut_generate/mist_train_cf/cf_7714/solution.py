"""
QUESTION:
Create a function `filter_and_sort_students` that takes a list of dictionaries representing students with 'name' and 'grade' keys. Return a new list of dictionaries where the 'name' key has "student_" added to the beginning, but only for students with a grade higher than 80. The list should be sorted in descending order by grade, and for students with the same grade, sorted in ascending order by name.
"""

def filter_and_sort_students(students):
    return sorted(
        [{'name': 'student_' + student['name'], 'grade': student['grade']} 
         for student in students if student['grade'] > 80], 
        key=lambda x: (-x['grade'], x['name'])
    )