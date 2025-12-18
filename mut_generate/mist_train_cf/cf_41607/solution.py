"""
QUESTION:
Create a function `filter_students` that takes in a list of student dictionaries and an age threshold as input, and returns a new list of dictionaries containing only the students whose age is less than the given threshold. Each dictionary in the returned list should contain the keys 'name', 'age', 'class', 'student_id', and 'profile_picture'.
"""

def filter_students(students, age_threshold):
    filtered_students = []
    for student in students:
        if student['age'] < age_threshold:
            filtered_students.append({
                'name': student['name'],
                'age': student['age'],
                'class': student['class'],
                'student_id': student['student_id'],
                'profile_picture': student['profile_picture']
            })
    return filtered_students