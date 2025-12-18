"""
QUESTION:
Write a function `solve_problem` that takes a JSON string as input, representing a list of students with their attributes and pastime activities. The function should return a tuple containing the duration in years of the second pastime activity of the first student and the overall average duration across all pastime activities of all students. Assume the JSON data is well-formed and each student has at least one hobby.
"""

import json

def solve_problem(data):
    students = json.loads(data)
    total_duration = 0
    count = 0
    first_student_second_hobby_duration = 0

    for i, student in enumerate(students):
        for j, hobby in enumerate(student["hobbies"]):
            if i == 0 and j == 1:
                first_student_second_hobby_duration = hobby["hobbyAge"]
            total_duration += hobby["hobbyAge"]
            count += 1

    average_duration = total_duration / count
    return first_student_second_hobby_duration, average_duration