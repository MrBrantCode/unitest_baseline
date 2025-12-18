"""
QUESTION:
Write a function `get_students` that takes an optional `name` filter, `age_min` filter, and `age_max` filter, and returns a list of students sorted in descending order of their ages. The function should be able to handle large amounts of data efficiently with a time complexity of O(nlogn) or better. 

The function should be able to filter the list of students based on the specified criteria. If `name` filter is provided, only include students whose names contain the specified name. If `age_min` filter is provided, only include students whose ages are greater than or equal to the specified age. If `age_max` filter is provided, only include students whose ages are less than or equal to the specified age.

Assume the input is a list of dictionaries, where each dictionary represents a student with `name` and `age` keys.
"""

def get_students(students, name=None, age_min=None, age_max=None):
    filtered_students = []
    for student in students:
        if name and name.lower() not in student['name'].lower():
            continue
        if age_min and student['age'] < age_min:
            continue
        if age_max and student['age'] > age_max:
            continue
        filtered_students.append(student)
    
    return sorted(filtered_students, key=lambda x: x['age'], reverse=True)